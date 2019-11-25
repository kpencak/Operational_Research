import numpy
from scipy.optimize import linprog

# kolejność strategii dla graczy: (1,2), (1,3), (2,3), (2,4)
A1 = numpy.array([[0, 2, -3, 0],
                 [-2, 0, 0, 3],
                 [3, 0, 0, -4],
                 [0, -3, 4, 0]])

A1 = numpy.transpose(A1)

b = numpy.array([-1, -1, -1, -1])

c = numpy.array([1, 1, 1, 1])

shift = numpy.abs(numpy.min(A1))
A1 += shift
A1 *= (-1)

result = linprog(c, A1, b).x

sum = result[0] + result[1] + result[2] + result[3]
v0 = (1/sum)
v = v0 - shift
numpy.set_printoptions(precision=4, suppress=True)
print("Gracz 1")
print("Result vector: ", result)
print("Prawdopodobieństwo 1: ", round(result[0]*v0, 3))
print("Prawdopodobieństwo 2: ", round(result[1]*v0, 3))
print("Prawdopodobieństwo 3: ", round(result[2]*v0, 3))
print("Prawdopodobieństwo 4: ", round(result[3]*v0, 3))
print("Wartość gry: ", round(v, 2))


A2 = numpy.array([[0, 2, -3, 0],
                 [-2, 0, 0, 3],
                 [3, 0, 0, -4],
                 [0, -3, 4, 0]])

A2 = numpy.transpose(A2)

shift = numpy.abs(numpy.min(A2))
A2 += shift
b *= (-1)
c *= (-1)

result = linprog(c, A2, b).x

sum = result[0] + result[1] + result[2] + result[3]
v0 = (1/sum)
v = v0 - shift
numpy.set_printoptions(precision=4, suppress=True)
print("Gracz 2")
print("Result vector: ", result)
print("Prawdopodobieństwo 1: ", round(result[0]*v0, 3))
print("Prawdopodobieństwo 2: ", round(result[1]*v0, 3))
print("Prawdopodobieństwo 3: ", round(result[2]*v0, 3))
print("Prawdopodobieństwo 4: ", round(result[3]*v0, 3))
print("Wartość gry: ", round(v, 2))
