import numpy
from scipy.optimize import linprog
from scipy.linalg import solve

# 0.5A + 0.4B + 0.4C + 0.2D <= 2000
# 0.4A + 0.2B + 0C + 0.5D <= 2800

# 10A + 14B + 8C + 11D -> max

# A, B, C, D => 0

A = numpy.array([[0.5, 0.4],
                 [0.4, 0.2],
                 [0.4, 0],
                 [0.2, 0.5],
                 [1, 0],
                 [0, 1]])

b = numpy.array([2000, 2800])

c = numpy.array([10, 14, 8, 11, 0, 0])

A *= -1
c *= -1

result = linprog(b, A, c).x
print(result)
sum = 0
for i in range(numpy.size(b)):
    print("y[", i, "] =", result[i])
    sum += b[i]*result[i]
print("Value of target function:", round(sum, 2))

# deleting inequalities where inequality is >
D = []
E = []
columns = numpy.size(A, 1)
rows = numpy.size(A, 0)
for i in range(rows-2):
    sum2 = 0
    for j in range(columns):
        sum2 += A[i][j]*round(result[j], 2)
    if sum2 >= c[i]:    #bo ujemne wartości
        D.append(A[i][:])
        E.append(c[i])
    else:
        print("Deleted inequation:", i+1)

D = numpy.asarray(D)*(-1)
E = numpy.asarray(E)

print("New values of matrix D = ", D)
print("New values of objective function E = ", E)

result = linprog(E, D, b).x
print("A = 0")
print("B = ", round(result[0], 2))
print("C = 0")
print("D = ", round(result[1], 2))
print("Value of target function:", round(sum, 2))