import falcon

from predict_square.predict import Predictor

class PredictResource:
    def __init__(self):
        self.predictor = Predictor()

    def on_post(self, req, resp):
        data = req.media.get("data")
        if data is not None:
            output = {}
            if isinstance(data, list):
                output["data"] = self.predictor.predict(data)
            else:
                pass
            resp.media = output

        else:
            raise falcon.HTTPBadRequest(
                "400 Bad Request", "Request body has no data key"
            )
