from matrix import Matrix


class Perceptron:
    class Layer:
        def __init__(self, num_inputs, num_outputs, bias, activation_function):
            self.weights = Matrix(num_outputs, num_inputs)
            self.weights.init_random()
            self.bias = Matrix.initialized(num_outputs, 1, bias)
            self.activation_function = activation_function

    def __init__(self, **kwargs):
        self.layer_associative = Layer(kwargs["count_associative_inputs"],
                                       kwargs["count_associative_outputs"],
                                       kwargs.get("bias_associative", 0.1),
                                       lambda x: 0 if x < 0 else (1 if x > 1 else x))

        self.layer_resultant = Layer(kwargs["count_associative_outputs"],
                                     kwargs["count_resultant_outputs"],
                                     kwargs.get("bias_resultant", 0.1),
                                     lambda x: 0 if x < 0 else 1)

