import numpy
from scipy.optimize import linprog

A = numpy.array([[1, 4],
                 [3, 6],
                 [2, 5],
                 [3, 7],
                 [1, 1],
                 [1, 0],
                 [0, 1]])

b = numpy.array([2, 5, 3, 4, 1, 0, 0])

c = [6, 15]

A *= -1
b *= -1

result = linprog(c, A, b).x
print(result)
sum = 0
for i in range(numpy.size(c)):
    print(result[i])
    sum += c[i]*result[i]
print(round(sum, 2))

