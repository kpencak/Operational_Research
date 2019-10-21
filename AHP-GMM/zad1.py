import numpy
from numpy import linalg as lin
import math
from scipy import stats as stats

c = numpy.array([[1, 4, 7, 5, 8, 6, 6, 2],
     [1/4, 1, 5, 3, 7, 6, 6, 1/3],
     [1/7, 1/5, 1, 1/3, 5, 3, 3, 1/5],
     [1/5, 1/3, 3, 1, 6, 3, 4, 1/2],
     [1/8, 1/7, 1/5, 1/6, 1, 1/3, 1/4, 1/7],
     [1/6, 1/6, 1/3, 1/3, 3, 1, 1/2, 1/5],
     [1/6, 1/6, 1/3, 1/4, 4, 2, 1, 1/5],
     [1/2, 3, 5, 2, 7, 5, 5, 1]])

c1 = [[1, 1/ 7, 1/5],
      [7, 1, 3],
      [5, 1/3, 1]]

c2 = [[  1,   5, 9],
      [1/5,   1, 4],
      [1/9, 1/4, 1]]

c3 = [[  1, 4, 1/5],
      [1/4, 1, 1/9],
      [  5, 9,   1]]

c4 = [[  1, 9,   4],
      [1/9, 1, 1/4],
      [1/4, 4,   1]]

c5 = [[1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]]

c6 = [[  1, 6, 4],
      [1/6, 1, 1/3],
      [1/4, 3, 1]]

c7 = [[  1, 9, 6],
      [1/9, 1, 1/3],
      [1/4, 3, 1]]

c8 = [[1, 1/2, 1/2],
      [2, 1, 1],
      [2, 1, 1]]

macierze = [c1, c2, c3, c4, c5, c6, c7, c8]
def gmm(matrix):
    vector_matrix = []
    n = numpy.size(matrix, 1)
    for i in range(n):
        result = stats.gmean(matrix[i])
        vector_matrix.append(result)
    sum_vector = numpy.sum(numpy.abs(vector_matrix))
    final_matrix = vector_matrix/sum_vector
    return final_matrix


vector1 = gmm(c1)
vector2 = gmm(c2)
vector3 = gmm(c3)
vector4 = gmm(c4)
vector5 = gmm(c5)
vector6 = gmm(c6)
vector7 = gmm(c7)
vector8 = gmm(c8)
vectorC = gmm(c)

big_matrix = numpy.column_stack((vector1, vector2, vector3, vector4, vector5, vector6, vector7, vector8))
result = big_matrix @ vectorC

print(result)
