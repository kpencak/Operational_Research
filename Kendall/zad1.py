import numpy
import math

A = numpy.array([[1, 2/3, 2, 5/2, 5/3, 5],
                 [3/2, 1, 3, 10/3, 3, 9],
                 [1/2, 1/3, 1, 4/3, 7/8, 5/2],
                 [2/5, 3/10, 3/4, 1, 5/6, 12/5],
                 [3/5, 1/3, 8/7, 6/5, 1, 3],
                 [1/5, 1/9, 2/5, 5/12, 1/3, 1]])

B = numpy.array([[1, 2/5, 3, 7/3, 1/2, 1, 2],
                 [5/2, 1, 4/7, 1, 1, 3, 2/3],
                 [1/3, 7/4, 1, 1/2, 2, 1/2, 1],
                 [3/7, 1, 2, 1, 4, 2, 6],
                 [2, 1, 1/2, 1/4, 1, 1/2, 3/4],
                 [1, 1/3, 2, 1/2, 2, 1, 5/8],
                 [1/2, 3/2, 1, 1/6, 4/3, 8/5, 1]])

C = numpy.array([[1, 2/3, 2/15, 1, 8, 12/5, 1, 1/2],
                 [3/2, 1, 1, 2, 1, 2/3, 1/6, 1],
                 [15/2, 1, 1, 5/2, 7/8, 2, 1, 1/5],
                 [1, 1/2, 2/5, 1, 4/3, 1, 2/7, 1],
                 [1/8, 1, 8/7, 3/4, 1, 1/5, 2/7, 1],
                 [5/12, 3/2, 1/2, 1, 5, 1, 3, 2],
                 [1, 6, 1, 7/2, 7/2, 1/3, 1, 3/11],
                 [2, 1, 5, 1, 1, 1/2, 11/3, 1]])

D = numpy.array([[0, 1, 1, -1, -1, 1, -1],
                 [-1, 0, 0, 1, 1, -1, 0],
                 [-1, 0, 0, 0, 1, 1, -1],
                 [1, -1, 0, 0, 1, 0, 1],
                 [1, 0, -1, -1, 0, 1, -1],
                 [-1, 1, -1, 1, -1, 0, 0],
                 [1, 0, 1, -1, 1, 0, 0]])

E = numpy.array([[0, 1, 0, 0, -1],
                 [-1, 0, 0, 0, 1],
                 [0, 0, 0, 1, 0],
                 [0, 0, -1, 0, 0],
                 [1, -1, 0, 0, 0]])

F = numpy.array([[0, -1, 1, -1, 1, -1, 1, -1, 1],
                 [1, 0, 1, 1, 1, -1, -1, -1, -1],
                 [-1, -1, 0, -1, 1, -1, 1, 1, 1],
                 [1, -1, 1, 0, -1, 1, -1, 1, -1],
                 [-1, -1, -1, 1, 0, -1, 1, 1, 1],
                 [1, 1, 1, -1, 1, 0, -1, -1, -1],
                 [-1, 1, -1, 1, -1, 1, 0, 1, -1],
                 [1, 1, -1, -1, -1, 1, -1, 0, 1],
                 [-1, 1, -1, 1, -1, 1, 1, -1, 0]])


def to_general_tournament_matrix(matrix):
    n = numpy.shape(matrix)[0]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
               matrix[i][j] = 0
            elif matrix[i][j] > 1:
                matrix[i][j] = 1
            else:
                matrix[i][j] = -1
    return matrix


def is_generalised(matrix):
    n = numpy.shape(matrix)[0]
    for i in range(n):
        for j in range(i+1):
            if i == j and matrix[i][j] != 0:
                return False
            elif matrix[i][j] != 1 and matrix[i][j] != -1 and matrix[i][j] != 0:
                return False
            elif matrix[i][j] != -matrix[j][i]:
                return False
    return True


def allow_ties(matrix):
    n = numpy.shape(matrix)[0]
    for i in range(n):
        for j in range(i+1):
            if i != j and matrix[i][j] == 0:
                return True
    return False


def classical_kendall_index(matrix):
    n = numpy.shape(matrix)[0]
    TMi = 0
    for i in range(n):
        # from i to n, 'cause first digit cannot reappear later
        for j in range(i, n):
            # from j to n, 'cause second digit cannot reappear later on different place
            for k in range(j, n):
                if i != j != k:
                    if matrix[i][j] == matrix[j][k] and matrix[j][k] == matrix[k][i]:
                        TMi += 1

    if (n % 2) != 0:
        I = (math.pow(n, 3) - n)/24
    else:
        I = (math.pow(n, 3) - 4*n)/24

    ksi = 1 - (TMi/I)
    return ksi


def generalised_kendall_index(matrix):
    n = numpy.shape(matrix)[0]
    TMi = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if i != j != k:
                    if (matrix[i][j] == matrix[j][k] == 0 and matrix[k][i] != 0) or (  # 1
                            matrix[j][k] == matrix[k][i] == 0 and matrix[i][j] != 0) or (
                            matrix[k][i] == matrix[i][j] == 0 and matrix[j][k] != 0):
                        TMi += 1
                    elif (matrix[i][j] == matrix[j][k] != 0 and matrix[k][i] == 0) or (   # 2
                            matrix[j][k] == matrix[k][i] != 0 and matrix[i][j] == 0) or (
                            matrix[k][i] == matrix[i][j] != 0 and matrix[j][k] == 0):
                        TMi += 1
                    elif matrix[i][j] == matrix[j][k] == matrix[k][i] != 0:  # 3
                        TMi += 1

    if n % 4 == 0:
        y = (13 * math.pow(n, 3) - 24 * math.pow(n, 2) - 16 * n) / 96
    elif n % 4 == 1:
        y = (13 * math.pow(n, 3) - 24 * math.pow(n, 2) - 19 * n + 30) / 96
    elif n % 4 == 2:
        y = (13 * math.pow(n, 3) - 24 * math.pow(n, 2) - 4 * n) / 96
    else:
        y = (13 * math.pow(n, 3) - 24 * math.pow(n, 2) - 19 * n + 18) / 96

    ksi = 1 - (TMi/y)
    return ksi


# 1
A = to_general_tournament_matrix(A)
B = to_general_tournament_matrix(B)
C = to_general_tournament_matrix(C)

# 2
print("Is D generalised? ", is_generalised(D))
print("Is E generalised? ", is_generalised(E))
print("Is F generalised? ", is_generalised(F), "\n")

# 3
print("Do A allow ties?: ", allow_ties(A))
print("Do B allow ties?: ", allow_ties(B))
print("Do C allow ties?: ", allow_ties(C))
print("Do E allow ties?: ", allow_ties(E))
print("Do F allow ties?: ", allow_ties(F), "\n")

# 4
print("Generalised Kendall Index for A: ", generalised_kendall_index(A))
print("Generalised Kendall Index for B: ", generalised_kendall_index(B))
print("Generalised Kendall Index for C: ", generalised_kendall_index(C))
print("Generalised Kendall Index for E: ", generalised_kendall_index(E))
print("Generalised Kendall Index for F: ", generalised_kendall_index(F), "\n")

# 5
print("Classical Kendall Index for A: ", classical_kendall_index(A))
print("Classical Kendall Index for F: ", classical_kendall_index(F))
