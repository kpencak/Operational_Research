import numpy
from scipy.optimize import linprog

# print("gwóźdż / cięcie  I | II | III | IV | V | VI | VII | VIII | IX | limit\n"
#       "  11             2 |  0 |  0  |  1 | 2 |  1 |  1  |   0  |  0 |  12 000\n"
#       "   8             1 |  3 |  0  |  2 | 0 |  1 |  0  |   2  |  1 |  24 000\n"
#       "   5             0 |  1 |  6  |  0 | 1 |  2 |  3  |   2  |  4 |  27 000\n"
#       "Odpadki:         0 |  1 |  0  |  3 | 3 |  1 |  4  |   4  |  2 |\n")
#
# print("Nierówności: \n"
#       "2x1 +     +     +  x4 + 2x5 +  x6 +  x7 +     +     = 12 000 \n"
#       " x1 + 3x2 +     + 2x4 +     +  x6 +     + 2x8 +  x9 = 24 000 \n"
#       "    +  x2 + 6x3 +     +  x5 + 2x6 + 3x7 + 2x8 + 4x9 = 27 000 \n"
#       "x1, x2, x3, x4, x5, x6, x7, x8, x9 >= 0")
#
# print("Funkcja celu: f(x) = x2 + 3x4 + 3x5 + x6 + 4x7 + 4x8 + 2x9 -> min")


A = numpy.array([[2, 1, 1, 0, 0, 0, 0, 2, 1],
                 [-2, -1, -1, 0, 0, 0, 0, -2, -1],
                 [1, 2, 1, 3, 2, 1, 0, 0, 0],
                 [-1, -2, -1, -3, -2, -1, 0, 0, 0],
                 [0, 0, 2, 1, 2, 4, 6, 1, 3],
                 [0, 0, -2, -1, -2, -4, -6, -1, -3]])
b = [12000, -12000, 24000, -24000, 27000, -27000]
c = numpy.array([0, -3, -1, -1, -4, -2, 0, -3, -4])

new_A = numpy.transpose(A)
new_b = numpy.transpose(c)
new_c = numpy.transpose(b)

result = linprog(new_c, -new_A, -new_b).x
print(result)
size = numpy.size(new_c)
sum = 0
for i in range(numpy.size(new_c)):
    print("y[", i, "] =", round(result[i]))
    sum += result[i]*new_c[i]
print("Value of target function:", round(sum))

# deleting inequalities where inequality is >
D = []
E = []
columns = numpy.size(new_A, 1)
rows = numpy.size(new_A, 0)

for i in range(rows):
    sum2 = 0
    for j in range(columns):
        sum2 += new_A[i][j]*result[j]
    print(sum2)
    if round(sum2, 2) <= new_b[i]:
        D.append(new_A[i][:])
        E.append(c[i])
    else:
        print("Deleted inequation:", i+1)

D = numpy.asarray(D)
D = numpy.transpose(D)
E = numpy.asarray(E)
E = numpy.transpose(E)

print("New values of matrix D = ", D)
print("New values of objective function E = ", E)
print("New values of matrix b = ", b)

result = numpy.linalg.lstsq(D, b, rcond=1)[0]
print(result)
print("[11 cm, 8 cm, 5 cm]")
print("I sposób: ", D[0], "kawałków: ", round(result[0], 2))
print("II sposób: ", D[2], "kawałków: ", round(result[1], 2))
print("III sposób: ", D[4], "kawałków: ",round(result[2], 2))
print("Value of target function:", round(-sum, 2))
