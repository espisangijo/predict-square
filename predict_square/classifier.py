import os
import pickle
import ast
from datetime import datetime

from .constant import ROOT_DIR, MODEL_DIR, DATA_DIR
from .utils import preprocess

from sklearn.svm import SVC

class SVMClassifier:

    def __init__(self, model_name='default'):
        self.model_dir = os.path.join(MODEL_DIR,'svm')
        self.kernel = 'linear'
        self.random_state = 42
        if model_name == 'default':
            self.__model = self.__load_models(self.latest())
        else:
            self.__model = self.__load_models(model_name)

    def latest(self):
        latest_dir = sorted(os.listdir(self.model_dir),reverse = True)[0]
        return latest_dir

    def __preprocess(self, data):
        data = preprocess(data)
        return data

    def __load_models(self, model_name):
        model_path = os.path.join(self.model_dir, model_name)
        model = pickle.load(open(model_path, 'rb'))
        return model

    def predict_proba(self, data):
        return self.__model.predict_proba([data])

    def predict(self, data):
        return self.__model.predict([data])

    def train_from_file(self, filename, checkpoint=None):
        X, y = [], []
        with open(os.path.join(DATA_DIR, filename), 'r') as f:
            data = f.read().splitlines()
            for d in data:
                d = d.split(' ')
                X.append(ast.literal_eval(''.join(d[1:])))
                y.append(d[0])


        if checkpoint == None:
            clf = SVC(kernel=self.kernel, random_state=self.random_state, probability=True)
        else:
            model_path = os.path.join(self.model_dir, checkpoint)
            clf = pickle.load(open(model_path, 'rb'))

        X = [self.__preprocess(x) for x in X]

        clf.fit(X, y)

        model_name = 'svm'
        version = datetime.now().strftime('%Y%m%d%H%M')

        svm_filename = os.path.join(MODEL_DIR, model_name, version)
        pickle.dump(clf, open(svm_filename, 'wb'))
