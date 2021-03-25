import numpy as np
from transformers import AutoTokenizer, AutoModelWithLMHead
from classifiers.classifiers import EmotionClassifier


def get_model():
    tokenizer = AutoTokenizer.from_pretrained("mrm8488/t5-base-finetuned-emotion")
    model = AutoModelWithLMHead.from_pretrained("mrm8488/t5-base-finetuned-emotion")
    return model, tokenizer


def get_emotion(text, model, tokenizer):
    input_ids = tokenizer.encode(text + '</s>', return_tensors='pt')

    output = model.generate(input_ids=input_ids,
                            max_length=2)

    dec = [tokenizer.decode(ids) for ids in output]
    label = dec[0]
    _, label = label.split()
    return label


class T5EmotionClassifier(EmotionClassifier):
    def __init__(self):
        self.model, self.tokenizer = get_model()
        self._labels = ['anger', 'fear', 'joy', 'love', 'sadness', 'surprise', 'other']

    def classify(self, text):
        return get_emotion(text, self.model, self.tokenizer)

    def classify_scores(self, text):
        pred = self.classify(text)
        if pred in self._labels:
            index = self._labels.index(pred)
        else:
            index = len(self._labels) - 1
            print('Unexpected prediction:', pred)
        scores = np.zeros(len(self._labels))
        scores[index] = 1
        return scores

    @property
    def labels(self):
        return self._labels
