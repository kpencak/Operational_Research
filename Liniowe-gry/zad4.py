import numpy
from scipy.optimize import linprog

A1 = numpy.array([[-2, 8, 2],
                 [3, -1, 0]])

b1 = [1, 1]
b2 = [-1, -1, -1]

c1 = [-1, -1, -1]
c2 = [1, 1]

shift = numpy.abs(numpy.min(A1))
A1 += shift
result = linprog(c1, A1, b1).x

sum = result[0] + result[1] + result[2]

v0 = 1/sum
v = v0 - shift
numpy.set_printoptions(precision=3, suppress=True)
print("Gracz 1")
print("Result vector: ", result)
print("Prawdopodobieństwo 1: ", round(result[0]*v0, 3))
print("Prawdopodobieństwo 2: ", round(result[1]*v0, 3))
print("Prawdopodobieństwo 3: ", round(result[2]*v0, 3))
print("Wartość gry: ", round(v, 2))

A2 = numpy.array([[-2, 8, 2],
                 [3, -1, 0]])

A2 = numpy.transpose(A2)

shift = numpy.abs(numpy.min(A2))
A2 += shift
A2 *= (-1)
result = linprog(c2, A2, b2).x

sum = result[0] + result[1]

v0 = (1/sum)
v = (1/sum) - shift
numpy.set_printoptions(precision=3, suppress=True)
print("Gracz 2")
print("Result vector: ", result)
print("Prawdopodobieństwo 1: ", round(result[0]*v0, 3))
print("Prawdopodobieństwo 2: ", round(result[1]*v0, 3))
print("Wartość gry: ", round(v, 2))