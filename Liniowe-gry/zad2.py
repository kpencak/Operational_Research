import numpy
from scipy.optimize import linprog

A = [[-5, -15],
     [-20, -5],
     [15, 2],
     [-1, 0],
     [0, -1]]

b = [-50, -40, 60, 0, 0]

c = [8, 4]

result = linprog(c, A, b).x
sum = 0
for i in range(numpy.size(c)):
    print(round(result[i], 2))
    sum += c[i]*result[i]
print(round(sum, 2))