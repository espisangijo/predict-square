import os
from .constant import ROOT_DIR, MODEL_DIR
import pickle


class SquareClassifier():
    def __init__(self, model_name='RNN'):
        self._model = self.__load_models(model_name)

    def __load_models(self, model_name):
        model_path = os.path.join(ROOT_DIR, model_name)

        return model_path

    def predict_proba(self, data):
        '''
        :param texts: ex. ["hello", "oke sist makasih"]
        :return: ex. [[('zh', 0.7506697773933411), ('th', 0.13971607387065887)],
                        [('en', 0.915301501750946), ('zh', 0.06814993172883987)]]
        '''
        model_results = self._model.predict(data)
        pred_probs = self.__format_answer(model_results)
        return pred_probs

class SVMClassifier():
    model_dir = os.path.join(MODEL_DIR,'svm')
    def __init__(self, model_name='default'):
        if model_name == 'default':
            self.__model = self.__load_models(self.latest())
        else:
            self.__model = self.__load_models(model_name)

    def latest(self):
        latest_dir = sorted(os.listdir(self.model_dir),reverse = True)[0]
        return latest_dir
        
    def __load_models(self, model_name):
        model_path = os.path.join(self.model_dir, model_name)
        model = pickle.load(open(model_path, 'rb'))
        return model

    def predict_proba(self, data):
        '''
        :param texts: ex. ["hello", "oke sist makasih"]
        :return: ex. [[('zh', 0.7506697773933411), ('th', 0.13971607387065887)],
                        [('en', 0.915301501750946), ('zh', 0.06814993172883987)]]
        '''
        
        model_results = self.__model.predict_proba(data)
        return model_results
    
    def predict(self, data):
        '''
        :param texts: ex. ["hello", "oke sist makasih"]
        :return: ex. [[('zh', 0.7506697773933411), ('th', 0.13971607387065887)],
                        [('en', 0.915301501750946), ('zh', 0.06814993172883987)]]
        '''
        
        model_results = self.__model.predict(data)
        return model_results