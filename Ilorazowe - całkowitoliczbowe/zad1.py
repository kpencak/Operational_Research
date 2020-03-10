import numpy
from scipy.optimize import linprog

A = [[-500, 1, 2],
     [-350, 1, 1],
     [600, -2, -2],
     [0, 1, 2],
     [0, -1, -2],
     [-1, 0, 0],
     [0, -1, 0],
     [0, 0, -1]]

b = [0, 0, 0, 1, -1, 0, 0, 0]

c = [0, -3, -4]

result = linprog(c, A, b, method='simplex').x
numpy.set_printoptions(suppress=True)
print(result)

x1 = result[1]/result[0]
x2 = result[2]/result[0]
z = (3*x1 + 4*x2)/(x1 + 2*x2)
print("x1 = ", x1)
print("x2 = ", x2)
print("z = ", z)
