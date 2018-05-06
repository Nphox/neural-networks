import perceptron


a = []

for i in range(100):
    a.append(i % 2)

p = perceptron.Perceptron(count_associative_inputs=100,
                          count_associative_outputs=128,
                          count_resultant_outputs=10,
                          bias_associative=0.1,
                          bias_resultant=0.1)

print(p.predict(a))
