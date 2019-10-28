import numpy
from numpy import linalg as lin
import math

A = numpy.array([[1, 2/3, 2, 5/2, 5/3, 5],
                  [3/2, 1, 3, 10/3, 3, 9],
                  [1/2, 1/3, 1, 4/3, 7/8, 5/2],
                  [2/5, 3/10, 3/4, 1, 5/6, 12/5],
                  [3/5, 1/3, 8/7, 6/5, 1, 3],
                  [1/5, 1/9, 2/5, 5/12, 1/3, 1]])

B = numpy.array([[1, 2/5, 3, 7/3, 1/2, 1],
                  [5/2, 1, 4/7, 5/8, 1/3, 3],
                  [1/3, 7/4, 1, 1/2, 2, 1/2],
                  [3/7, 8/5, 2, 1, 4, 2],
                  [2, 3, 1/2, 1/4, 1, 1/2],
                  [1, 1/3, 2, 1/2, 2, 1]])

C = numpy.array([[1, 17/4, 17/20, 8/5, 23/6, 8/3],
                  [4/17, 1, 1/5, 2/5, 9/10, 2/3],
                  [20/17, 5, 1, 21/10, 51/10, 10/3],
                  [5/8, 5/2, 10/21, 1, 5/2, 11/6],
                  [6/23, 10/9, 10/51, 2/5, 1, 19/30],
                  [3/8, 3/2, 3/10, 6/11, 30/19, 1]])

WA = numpy.array([[3],
                  [1]])
WB = numpy.array([[2],
                  [1/2],
                  [1]])
WC = numpy.array([[2],
                  [5]])


def rearrangeMatrix(matrix, values, size):
    rowMatrix = numpy.empty((0, size))
    for i in values:
        row = numpy.asmatrix(matrix[i-1])
        rowMatrix = numpy.vstack((rowMatrix, row))
    k = numpy.shape(values)[0]
    for i in range(k, 0, -1):
        index = values[i-1]-1
        matrix = numpy.delete(matrix, index, 0)
    matrix = numpy.asarray(numpy.vstack((matrix, rowMatrix)))

    columnMatrix = numpy.empty((size, 0))
    for i in values:
        column = numpy.asarray(matrix[:, i-1])
        columnMatrix = numpy.column_stack((columnMatrix, column))
    for i in range(k, 0, -1):
        index = values[i-1]-1
        matrix = numpy.delete(matrix, index, 1)
    matrix = numpy.asarray(numpy.column_stack((matrix, numpy.asmatrix(columnMatrix))))

    return matrix


def koczkodaj(matrix):
    n = numpy.size(matrix, 1)
    vector = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                product = (matrix[i][k]*matrix[k][j])/matrix[i][j]
                minimum = min(numpy.abs(1-product), numpy.abs(1-(1/product)))
                vector.append(minimum)
    result = max(vector)
    return result


def isRearranged(vector, W, valuesC):
    n = numpy.size(valuesC, 0)
    for i in range(0, n):
        W = numpy.insert(W, valuesC[i]-1, vector[i])
    return W


def HRE_aryt(matrix, vector, *args, **kwargs):
    n = numpy.shape(matrix)[0]
    k = numpy.shape(vector)[0]
    if 'is_rearranged' in kwargs and kwargs['is_rearranged'] == True:
        matrix = rearrangeMatrix(matrix, kwargs['valuesC'], n)

    koczkodaj_index = koczkodaj(matrix)
    if koczkodaj_index < (1 - ((1+math.sqrt(4*(n-1)*(n-k-2)))/(2*(n-1)))):
        print("Wyliczony indeks jest mniejszy, więc metoda ma poprawne rozwiązanie")
    else:
        print("Wyliczony indeks jest większy, więc metoda daje wynik niezbyt godny zaufania")
    newMatrix = matrix[range(0, n-k)]
    matrixA = newMatrix[:, range(0, n-k)]
    matrixB = newMatrix[:, range(n-k, n)]
    for i in range(n-k):
        for j in range(n-k):
            if i != j:
                matrixA[i][j] *= (-1/(n-1))
    matrixB = (matrixB @ vector) * (1/(n-1))
    W = lin.solve(matrixA, matrixB)
    if 'is_rearranged' in kwargs and kwargs['is_rearranged'] == True:
        result = isRearranged(vector, W, kwargs['valuesC'])
    else:
        result = numpy.vstack((W, vector))
    return result


arytA = HRE_aryt(A, WA)
print("Arytmetyczna A: ", arytA, "\n")
arytB = HRE_aryt(B, WB)
print("Arytmetyczna B: ", arytB, "\n")

valuesC = [2, 4]
arytC = HRE_aryt(C, WC, is_rearranged=True, valuesC=valuesC)
print("Arytmetyczna C: ", arytC, "\n")