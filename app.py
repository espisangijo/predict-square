import falcon

from predict_square.resources.predict_resource import PredictResource
from predict_square.resources.preprocess_resource import PreprocessResource
from predict_square.resources.healthcheck_resource import HealthCheckResource
from predict_square.resources.train_resource import TrainResource

api = falcon.API()
api.add_route("/", HealthCheckResource())
api.add_route("/predict", PredictResource())
api.add_route("/preprocess", PredictResource())
api.add_route("/train", TrainResource())
