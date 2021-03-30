from abc import ABC


class Classifier:
    def classify(self, text):
        raise NotImplementedError

    def classify_scores(self, text):
        raise NotImplementedError

    @property
    def labels(self):
        raise NotImplementedError


class SentimentClassifier(Classifier, ABC):
    pass


class EmotionClassifier(Classifier, ABC):
    pass
