import numpy
from numpy import linalg as lin

A = [[1, 7, 3],
     [1/7, 1, 2],
     [1/3, 1/2, 1]]

B = [[1, 1/5, 7, 1],
     [5, 1, 1/2, 2],
     [1/7, 2, 1, 3],
     [1, 1/2, 1/3, 1]]

C = [[1, 2, 5, 1, 7],
     [1/2, 1, 3, 1/2, 5],
     [1/5, 1/3, 1, 1/5, 2],
     [1, 2, 5, 1, 7],
     [1/7, 1/5, 1/2, 1/7, 1]]

test = [[1, 3, 1/2, 5],
        [1/3, 1, 1/6, 2],
        [2, 6, 1, 9],
        [1/5, 1/2, 1/9, 1]]


def satty_index(matrix):
    n = numpy.size(matrix, 1)
    w, v = lin.eig(matrix)
    lambdaMax = numpy.amax(w)
    CI = (lambdaMax - n) / (n - 1)
    return CI.real


indexA = satty_index(A)
indexB = satty_index(B)
indexC = satty_index(C)
indextest = satty_index(test)

print(indexA, indexB, indexC, indextest)