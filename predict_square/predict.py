import os
from .classifier import SVMClassifier
from .utils import interpolate, normalize, skinny

class Predictor:
    def __init__(self, classifier=SVMClassifier()):
        self.__clf = classifier

    def __preprocess(self, data):
        normalized_data = normalize(data)
        interpolated_data = interpolate(normalized_data, 100)
        skinny_data = skinny(interpolated_data)

        return skinny_data

    def predict(self, data):
        data = self.__preprocess(data)
        prediction = self.__clf.predict(data)
        return prediction

    def predict_proba(self, data):
        data = self.__preprocess(data)
        prediction = self.__clf.predict_proba(data)
        return prediction

if __name__ == '__main__':
    some_input = []
    predictor = Predictor()
    print(predictor.predict_proba(some_input))
