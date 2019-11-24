import numpy
from scipy.optimize import linprog

A = [[1, 1, 1],
     [-1, -1, -1],
     [-1, -2, -1],
     [0, 2, 1],
     [-1, 0, 0],
     [0, -1, 0],
     [0, 0, -1]]

b = [30, -30, -10, 20, 0, 0, 0]

c = [-2, -1, -3]

result = linprog(c, A, b).x
sum = 0
for i in range(numpy.size(c)):
     print(round(result[i]))
     sum += -c[i]*result[i]
print(round(sum))