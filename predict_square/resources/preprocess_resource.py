import falcon

from predict_square.predict import Predictor
from predict_square.constant import DATA_DIR

class PreprocessResource:
    def on_post(self, req, resp):
        with open(os.path.join(DATA_DIR, 'square.json'), 'r') as f:
            square_data = json.load(f)["data"]
        with open(os.path.join(DATA_DIR, 'notsquare.json'), 'r') as f:
            notsquare_data = json.load(f)["data"]

        with open(os.path.join(DATA_DIR,'train.txt'),'w') as f:
            for i in range(len(square_data)):
                f.write('__label__square {}\n'.format(square_data[i]))
                f.write('__label__nsquare {}\n'.format(notsquare_data[i]))
