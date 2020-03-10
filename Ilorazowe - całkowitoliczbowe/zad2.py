import numpy
from scipy.optimize import linprog

A = [[-9000, 2, 1],
     [-5500, 1, 1],
     [-10000, 1, 2.5],
     [0, 140, 250],
     [0, -140, -250],
     [100, -1, 0],
     [100, 0, -1]]

b = [0, 0, 0, 1, -1, 0, 0]

c = [0, -150, -130]

result = linprog(c, A, b, method='simplex').x
numpy.set_printoptions(suppress=True)
print(result)

x1 = result[1]/result[0]
x2 = result[2]/result[0]
z = (150*x1 + 130*x2)/(140*x1 + 250*x2)
print("x1 = ", x1)
print("x2 = ", x2)
print("z = ", z)
