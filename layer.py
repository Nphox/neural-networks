from matrix import Matrix

EPS = 0.1

class Layer:
    def __init__(self, num_inputs, num_outputs, activation_function, init_flag = True):
        self.weights = Matrix(num_outputs, num_inputs)
        if init_flag:
            self.weights.init_random()
        self.activation_function = activation_function

    def predict(self, vect):
        res = self.weights * vect
        res.apply_func(self.activation_function)
        return res

    def train(self, err):
        for i in range(len(err)):
            if abs(err.items[i]) < 1e-5:
                continue
            row_diff = EPS if err.items[i] < 0 else -EPS

            for j in range(self.weights.num_rows):
                self.weights.items[j][i] += row_diff




