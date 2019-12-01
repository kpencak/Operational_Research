import numpy
from scipy.optimize import linprog

print("arkusz / belka  2.1   |      4.2 \n"
      "0.5            4    1 | 8   0   5   2 \n"
      "1.4            0    1 | 0   3   1   2 \n"
      "Odpadki:       0.1 0.2|0.2  0  0.3 0.4 \n")

print("Nierówności: \n"
      "4x1 + x2 + 8x3 +       5x5 + 2x6 >= 12 000 \n"
      "      x2 +       3x4 + x5 + 2x6 >= 18 000 \n"
      "x1, x2, x3, x4, x5, x6 >= 0")

print("Funkcja celu: f(x) = 0.1x1 + 0.2x2 + 0.2x3 + 0.3x5 + 0.4x6 -> min")


A = numpy.array([[-4, 0],
                 [-1, -1],
                 [-8, -0],
                 [0, -3],
                 [-5, -1],
                 [-2, -2],
                 [-1, 0],
                 [0, -1]])

b = numpy.array([-0.1, -0.2, -0.2, 0, -0.3, -0.4, 0, 0])

c = numpy.array([-12000, -18000])

result = linprog(c, A, b).x
print(result)
sum = 0
for i in range(numpy.size(c)):
    print("y[", i, "] =", result[i])
    sum += c[i]*result[i]
print("Value of target function:", round(sum, 2))

# deleting inequalities where inequality is >
D = []
E = []
columns = numpy.size(A, 1)
rows = numpy.size(A, 0)
A *= -1
b *= -1

for i in range(rows-2):
    sum2 = 0
    for j in range(columns):
        sum2 += A[i][j]*round(result[j], 2)
    print(sum2)
    if sum2 <= b[i]:
        D.append(A[i][:])
        E.append(b[i])
    else:
        print("Deleted inequation:", i+1)

D = numpy.asarray(D)
E = numpy.asarray(E)

print("New values of matrix D = ", D)
print("New values of objective function E = ", E)

result = linprog(c, D, E).x
print("A = 0")
print("B = ", round(result[0], 2))
print("C = 0")
print("D = ", round(result[1], 2))
print("Value of target function:", round(sum, 2))