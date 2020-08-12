import falcon

from predict_square.classifier import SVMClassifier

class TrainResource:
    def __init__(self):
        self.__clf = SVMClassifier()

    def on_post(self, req, resp):
        fn = req.media.get("filename")
        cp = req.media.get("checkpoint")
        self.__clf.train_from_file(fn, cp)
