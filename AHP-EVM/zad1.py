import numpy
from numpy import linalg as lin

c = [[1,     4,   7,   5, 8,   6,   6,   2],
     [1/4,   1,   5,   3, 7,   6,   6, 1/3],
     [1/7, 1/5,   1, 1/3, 5,   3,   3, 1/5],
     [1/5, 1/3,   3,   1, 6,   3,   4, 1/2],
     [1/8, 1/7, 1/5, 1/6, 1, 1/3, 1/4, 1/7],
     [1/6, 1/6, 1/3, 1/3, 3,   1, 1/2, 1/5],
     [1/6, 1/6, 1/3, 1/4, 4,   2,   1, 1/5],
     [1/2,   3,   5,   2, 7,   5,   5,   1]]

c1 = [[1, 1/7, 1/5],
      [7,   1,   3],
      [5, 1/3,   1]]
      
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

c6 = [[  1, 6,   4],
      [1/6, 1, 1/3],
      [1/4, 3,   1]]

c7 = [[  1, 9,   6],
      [1/9, 1, 1/3],
      [1/4, 3,   1]]

c8 = [[1, 1/2, 1/2],
      [2,   1,   1],
      [2,   1,   1]]

#wektory własne w - wartości własne, v - wektory własne
w1, v1 = lin.eig(c1)
w2, v2 = lin.eig(c2)
w3, v3 = lin.eig(c3)
w4, v4 = lin.eig(c4)
w5, v5 = lin.eig(c5)
w6, v6 = lin.eig(c6)
w7, v7 = lin.eig(c7)
w8, v8 = lin.eig(c8)

#wybieramy największa? wartość i wektor z nim,
index1 = numpy.argmax(w1)
index2 = numpy.argmax(w2)
index3 = numpy.argmax(w3)
index4 = numpy.argmax(w4)
index5 = numpy.argmax(w5)
index6 = numpy.argmax(w6)
index7 = numpy.argmax(w7)
index8 = numpy.argmax(w8)

#normalizujemy go
wektor1 = lin.eig(c1)[1][:, index1]
sum1 = numpy.sum(numpy.abs(wektor1))
wektor1 = wektor1/sum1

wektor2 = lin.eig(c2)[1][:, index2]
sum2 = numpy.sum(numpy.abs(wektor2))
wektor2 = wektor2/sum2

wektor3 = lin.eig(c3)[1][:, index3]
sum3 = numpy.sum(numpy.abs(wektor3))
wektor3 = wektor3/sum3

wektor4 = lin.eig(c4)[1][:, index4]
sum4 = numpy.sum(numpy.abs(wektor4))
wektor4 = wektor4/sum4

wektor5 = lin.eig(c5)[1][:, index5]
sum5 = numpy.sum(numpy.abs(wektor5))
wektor5 = wektor5/sum5

wektor6 = lin.eig(c6)[1][:, index6]
sum6 = numpy.sum(numpy.abs(wektor6))
wektor6 = wektor6/sum6

wektor7 = lin.eig(c7)[1][:, index7]
sum7 = numpy.sum(numpy.abs(wektor7))
wektor7 = wektor7/sum7

wektor8 = lin.eig(c8)[1][:, index8]
sum8 = numpy.sum(numpy.abs(wektor8))
wektor8 = wektor8/sum8

#wektor kryteriów, czyli po normalizacji
vector_matrix = numpy.column_stack((wektor1, wektor2, wektor3, wektor4, wektor5, wektor6, wektor7, wektor8))

wc, vc = lin.eig(c)
indexC = numpy.argmax(wc)
wektorC = lin.eig(c)[1][:, indexC]
sumC = numpy.sum(numpy.abs(wektorC))
wektorC = wektorC/sumC

result = vector_matrix @ wektorC

print(numpy.real(result))

#bierzemy wektor rang z wektoróœ znormalizowanych
#robimy to samo z dużą macierzą
#dzielimy wektor 8x1, z 8x1?????/??????/ 