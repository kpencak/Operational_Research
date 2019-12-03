import numpy
from scipy.optimize import linprog

print("arkusz / belka  2.1   |      4.2 \n"
      "0.5            4    1 | 8    5    2    0\n"
      "1.4            0    1 | 0    1    2    3\n"
      "Odpadki:       0.1 0.2|0.2  0.3  0.4   0\n")

print("Nierówności: \n"
      "4x1 + x2 + 8x3 + 5x4 + 2x5      >= 12 000 \n"
      "      x2 +        x4 + 2x5 + 3x6 >= 18 000 \n"
      "x1, x2, x3, x4, x5, x6 >= 0")

print("Funkcja celu: f(x) = 0.1x1 + 0.2x2 + 0.2x3 + 0.3x4 + 0.4x5 -> min")


A = numpy.array([[4, 1, 8, 5, 2, 0], [0, 1, 0, 1, 2, 3]]) * -1
b = numpy.array([[12000], [18000]]) * -1
c = numpy.array([0.1, 0.2, 0.2, 0.3, 0.4, 0]) * -1

new_A = numpy.transpose(A) * -1
new_b = numpy.transpose(c).reshape([c.size, 1]) * -1
new_c = numpy.transpose(b)

result = linprog(new_c, new_A, new_b).x
print(result)
size = numpy.size(new_c)
for i in range(numpy.size(new_c)):
    print("y[", i, "] =", result[i])
sum = result[0]*new_c[0][0] + result[1]*new_c[0][1]
print("Value of target function:", round(sum, 2))

# deleting inequalities where inequality is >
D = []
E = []
columns = numpy.size(new_A, 1)
rows = numpy.size(new_A, 0)

for i in range(rows):
    sum2 = 0
    for j in range(columns):
        sum2 += new_A[i][j]*round(result[j], 2)
    print(sum2)
    if sum2 >= new_b[i]:
        D.append(-new_A[i][:])
        E.append(c[i])
    else:
        print("Deleted inequation:", i+1)

D = numpy.asarray(D)
D = numpy.transpose(D)
E = numpy.asarray(E)
E = numpy.transpose(E)
print("New values of matrix D = ", D)
print("New values of objective function E = ", E)

result = linprog(E, A_eq=D, b_eq=b).x
print(result)
print("A = ", round(result[0], 2))
print("B = 0")
print("C = ", round(result[1], 2))
print("D = 0")
print("E = 0")
print("F = ", round(result[2], 2))
print("Value of target function:", round(-sum, 2))
