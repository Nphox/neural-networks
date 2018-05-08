import random
from vector import Vector


LOW_RANDOM = -0.05
HIGH_RANDOM = 0.05

class Matrix:
    def __init__(self, num_rows, num_cols):
        self.items = [[0 for i in range(num_cols)] for j in range(num_rows)]
        self.num_rows = num_rows
        self.num_cols = num_cols

    def init_random(self):
        for i in range(0, self.num_rows):
            for j in range(0, self.num_cols):
                self.items[i][j] = random.uniform(LOW_RANDOM, HIGH_RANDOM)

    def __mul__(self, other):
        other = other.items
        length = len(other)

        assert(length > 0)
        assert(length == self.num_cols)

        res = [0 for k in range(self.num_rows)]

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                res[i] += self.items[i][j] * other[j]

        return Vector(res)