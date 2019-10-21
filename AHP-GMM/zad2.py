import numpy
from numpy import linalg as lin
from scipy import stats as stats
import math

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


def gmm(matrix):
    vector_matrix = []
    n = numpy.size(matrix, 1)
    for i in range(n):
        result = stats.gmean(matrix[i])
        vector_matrix.append(result)
    sum_vector = numpy.sum(numpy.abs(vector_matrix))
    final_matrix = vector_matrix/sum_vector
    return final_matrix


def geo_index(matrix):
    n = numpy.size(matrix, 1)
    vector = gmm(matrix)
    sum = 0
    for i in range(n):
        for j in range(i+1, n):
            sum += math.pow(math.log10(matrix[i][j]*(vector[j]/vector[i])), 2)
    IG = 2/((n-1)*(n-2))*sum
    return IG


indexA = satty_index(A)
indexB = satty_index(B)
indexC = satty_index(C)
indextest = satty_index(test)

#index_geo_A = geo_index(A)
index_geo_test = geo_index(test)
print(index_geo_test)