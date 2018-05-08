from perceptron import Perceptron
from vector import Vector

ai = 10
ao = 16
ro = 5

f1 = lambda x: 0 if x < 0 else 1
f2 = lambda x: -1 if x < 0 else 1

a = Vector([1, 0, 0, 1, 0, 0, 1, 0, 0, 1])
b = Vector([-1, 1, -1, -1, -1])

p = Perceptron(ai, ao, ro, f1, f2)
for i in range(20):
    p.train(a, b)

print(p.predict(a))
