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
    for i in range(1, n):
        for j in range(i+1, n):
            sum += math.pow(math.log10(matrix[i][j]*(vector[j]/vector[i])), 2)
    IG = 2/((n-1)*(n-2))*sum
    return IG


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
    
indexA = satty_index(A)
indexB = satty_index(B)
indexC = satty_index(C)
print("Indeks Satty'ego dla macierzy A: ", indexA, "\n",
      "Indeks Satty'ego dla macierzy B: ", indexB, "\n",
      "Indeks Satty'ego dla macierzy C: ", indexC)

index_geo_A = geo_index(A)
index_geo_B = geo_index(B)
index_geo_C = geo_index(C)
print("Indeks geometryczny dla macierzy A: ", index_geo_A, "\n",
      "Indeks geometryczny dla macierzy B: ", index_geo_B, "\n",
      "Indeks geometryczny dla macierzy C: ", index_geo_C)

index_kocz_A = koczkodaj(A)
index_kocz_B = koczkodaj(B)
index_kocz_C = koczkodaj(C)
print("Indeks Koczkodaja dla macierzy A: ", index_kocz_A, "\n",
      "Indeks Koczkodaja dla macierzy B: ", index_kocz_B, "\n",
      "Indeks Koczkodaja dla macierzy C: ", index_kocz_C)