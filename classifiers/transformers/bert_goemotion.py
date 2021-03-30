"""
code taken from https://github.com/monologg/GoEmotions-pytorch
"""
from typing import Union, Optional

import numpy as np
import torch.nn as nn
from transformers import BertPreTrainedModel, BertModel
from transformers import BertTokenizer
from transformers import Pipeline, PreTrainedTokenizer, ModelCard
from transformers.pipelines import ArgumentHandler

from classifiers import EmotionClassifier


class BertForMultiLabelClassification(BertPreTrainedModel):
    def __init__(self, config):
        super().__init__(config)
        self.num_labels = config.num_labels

        self.bert = BertModel(config)
        self.dropout = nn.Dropout(config.hidden_dropout_prob)
        self.classifier = nn.Linear(config.hidden_size, self.config.num_labels)
        self.loss_fct = nn.BCEWithLogitsLoss()

        self.init_weights()

    def forward(
            self,
            input_ids=None,
            attention_mask=None,
            token_type_ids=None,
            position_ids=None,
            head_mask=None,
            inputs_embeds=None,
            labels=None,
    ):
        outputs = self.bert(
            input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            position_ids=position_ids,
            head_mask=head_mask,
            inputs_embeds=inputs_embeds,
        )
        pooled_output = outputs[1]

        pooled_output = self.dropout(pooled_output)
        logits = self.classifier(pooled_output)

        outputs = (logits,) + outputs[2:]  # add hidden states and attention if they are here

        if labels is not None:
            loss = self.loss_fct(logits, labels)
            outputs = (loss,) + outputs

        return outputs  # (loss), logits, (hidden_states), (attentions)


class MultiLabelPipeline(Pipeline):
    def __init__(
            self,
            model: Union["PreTrainedModel", "TFPreTrainedModel"],
            tokenizer: PreTrainedTokenizer,
            modelcard: Optional[ModelCard] = None,
            framework: Optional[str] = None,
            task: str = "",
            args_parser: ArgumentHandler = None,
            device: int = -1,
            binary_output: bool = False,
            threshold: float = 0.3
    ):
        super().__init__(
            model=model,
            tokenizer=tokenizer,
            modelcard=modelcard,
            framework=framework,
            args_parser=args_parser,
            device=device,
            binary_output=binary_output,
            task=task
        )

        self.threshold = threshold

    def __call__(self, *args, **kwargs):
        outputs = super().__call__(*args, **kwargs)
        scores = 1 / (1 + np.exp(-outputs))  # Sigmoid
        results = []
        for item in scores:
            labels = []
            scores = []
            for idx, s in enumerate(item):
                if s > self.threshold:
                    labels.append(self.model.config.id2label[idx])
                    scores.append(s)
            results.append({"labels": labels, "scores": scores})
        return results


class GoEmotionBertClassifier(EmotionClassifier):
    def __init__(self):
        tokenizer = BertTokenizer.from_pretrained("monologg/bert-base-cased-goemotions-original")
        model = BertForMultiLabelClassification.from_pretrained("monologg/bert-base-cased-goemotions-original")

        self.goemotions = MultiLabelPipeline(
            model=model,
            tokenizer=tokenizer,
            threshold=0.3
        )
        # https://github.com/monologg/GoEmotions-pytorch/blob/master/data/original/labels.txt
        self._labels = ['admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring', 'confusion', 'curiosity',
                        'desire', 'disappointment', 'disapproval', 'disgust', 'embarrassment', 'excitement', 'fear',
                        'gratitude', 'grief', 'joy', 'love', 'nervousness', 'optimism', 'pride', 'realization',
                        'relief', 'remorse', 'sadness', 'surprise', 'neutral']

    def classify(self, text):
        return np.argmax(self.classify_scores(text))

    def classify_scores(self, text):
        outputs = self.goemotions([text])[0]
        scores = np.zeros(len(self._labels))
        for i in range(len(outputs['labels'])):
            label = outputs['labels'][i]
            if label in self._labels:
                index = self._labels.index(label)
                scores[index] = outputs['scores'][i]
            else:
                index = len(self._labels) - 1
                scores[index] = outputs['scores'][i]
        return scores

    @property
    def labels(self):
        return self._labels
