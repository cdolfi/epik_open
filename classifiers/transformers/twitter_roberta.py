import csv
import urllib.request

import numpy as np
from scipy.special import softmax
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer

from classifiers.classifiers import EmotionClassifier, SentimentClassifier


def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)


def get_model(task='sentiment'):
    model_name = f"cardiffnlp/twitter-roberta-base-{task}"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    mapping_link = f"https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/{task}/mapping.txt"
    with urllib.request.urlopen(mapping_link) as f:
        html = f.read().decode('utf-8').split("\n")
        csvreader = csv.reader(html, delimiter='\t')
    labels = [row[1] for row in csvreader if len(row) > 1]

    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    model.save_pretrained(model_name)
    return model, tokenizer, labels


def classify(model, tokenizer, text):
    text = preprocess(text)
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    return scores


class TwitterRobertaBase:
    def __init__(self, task):
        self.model, self.tokenizer, self._labels = get_model(task)

    def classify_scores(self, text):
        return classify(self.model, self.tokenizer, text)

    def classify(self, text):
        scores = self.classify_scores(text)
        pred = np.argmax(scores)
        return pred

    @property
    def labels(self):
        return self._labels


class TwitterEmotionClassification(TwitterRobertaBase, EmotionClassifier):
    def __init__(self):
        super().__init__('emotion')


class TwitterSentimentClassification(TwitterRobertaBase, SentimentClassifier):
    def __init__(self):
        super().__init__('sentiment')
