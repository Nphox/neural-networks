
class Vector:
    def __init__(self, items):
        self.items = items

    def apply_func(self, func):
        for i in range(len(self.items)):
            self.items[i] = func(self.items[i])

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __sub__(self, other):
        assert(len(other) == len(self))
        return Vector([self.items[i] - other.items[i] for i in range(len(self.items))])