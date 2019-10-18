import numpy
from numpy import linalg as lin

C = [[  1,   5,   3, 4],
     [1/5,   1,   4, 1],
     [1/3, 1/4,   1, 2],
     [1/4,   1, 1/2, 1]]

c1 = [[  1, 1/5,   2, 4],
      [  5,   1,   7, 9],
      [1/2, 1/7,   1, 2],
      [1/4, 1/9, 1/2, 1]]

c2 = [[  1,   1,   3, 2],
      [  1,   1,   3, 2],
      [1/3, 1/3,   1, 2],
      [1/2, 1/2, 1/2, 1]]

c3 = [[  1, 3, 1/3, 1/6],
      [1/3, 1, 1/7, 1/9],
      [  3, 7,   1, 1/2],
      [  6, 9,   2,   1]]

c4 = [[1, 1/7, 1/2, 1/3],
      [7,   1,   5,   3],
      [2, 1/5,   1, 1/2],
      [3, 1/3,   2,   1]]

##wektory własne w - wartości własne, v - wektory własne 
w1, v1 = lin.eig(c1)
w2, v2 = lin.eig(c2)
w3, v3 = lin.eig(c3)
w4, v4 = lin.eig(c4)
wC, vC = lin.eig(C)

#wybieramy największa? wartość i wektor z nim,
index1 = numpy.argmax(w1)
index2 = numpy.argmax(w2)
index3 = numpy.argmax(w3)
index4 = numpy.argmax(w4)
indexC = numpy.argmax(wC)

#normalizujemy go
wektor1 = lin.eig(c1)[1][:, index1]
sum1 = numpy.sum(numpy.abs(wektor1))
wektor1 = numpy.abs(wektor1)/sum1

wektor2 = lin.eig(c2)[1][:, index2]
sum2 = numpy.sum(numpy.abs(wektor2))
wektor2 = numpy.abs(wektor2)/sum2

wektor3 = lin.eig(c3)[1][:, index3]
sum3 = numpy.sum(numpy.abs(wektor3))
wektor3 = numpy.abs(wektor3)/sum3

wektor4 = lin.eig(c4)[1][:, index4]
sum4 = numpy.sum(numpy.abs(wektor4))
wektor4 = numpy.abs(wektor4)/sum4

wektorC = lin.eig(C)[1][:, indexC]
sumC = numpy.sum(numpy.abs(wektorC))
wektorC = numpy.abs(wektorC)/sumC

#wektor kryteriów, czyli po normalizacji
vector_matrix = numpy.column_stack((wektor1, wektor2, wektor3, wektor4))
result = vector_matrix @ wektorC

print(numpy.real(result))