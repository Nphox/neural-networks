from layer import Layer


class Perceptron:
    def __init__(self, ai, ao, ro, f1, f2):
        self.layer_associative = Layer(ai, ao, f1)
        self.layer_resultant = Layer(ao, ro, f2, False)

    def predict(self, vect):
        res = self.layer_associative.predict(vect)
        return self.layer_resultant.predict(res)

    def train(self, in_vect, out_vect):
        res = self.predict(in_vect)
        err = out_vect - res
        self.layer_resultant.train(err)
        return self.predict(in_vect)