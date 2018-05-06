import random


class Matrix:
    def __init__(self, num_rows, num_cols):
        self.items = [[0 for i in range(num_cols)] for j in range(num_rows)]
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.LOW_RANDOM = -0.05
        self.HIGH_RANDOM = 0.05

    def init_random(self):
        for i in range(0, self.num_rows):
            for j in range(0, self.num_cols):
                self.items[i][j] = random.uniform(self.LOW_RANDOM, self.HIGH_RANDOM)

    def initialized(num_rows, num_cols, value):
        result = Matrix(num_rows, num_cols)
        for i in range(0, num_rows):
            for j in range(0, num_cols):
                result.__items__[i][j] = value
        return result
