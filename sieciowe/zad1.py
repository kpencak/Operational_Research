import numpy

a = numpy.array([3, 3, 7, 10, 1, 5, 6, 4, 1, 4, 10, 5, 5, 1])
m = numpy.array([4, 3, 9, 12, 5, 10, 12, 6, 1, 4, 15, 5, 8, 5])
b = numpy.array([5, 3, 17, 14, 9, 15, 18, 14, 7, 4, 20, 11, 11, 9])

te = numpy.empty(len(a))
sigma2 = numpy.empty(len(a))

for i in range(0, len(a)):
    te[i] = (a[i] + 4*m[i] + b[i])/6
    sigma2[i] = pow((b[i]-a[i])/6, 2)

print(numpy.round(te, 2))
print(numpy.round(sigma2, 2))