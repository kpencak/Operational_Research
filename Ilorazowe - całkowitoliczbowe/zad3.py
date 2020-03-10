import numpy
from scipy.optimize import linprog

#zadanie 1
A = [[4, 3],
     [1, 1],
     [-1, 0],
     [0, -1]]

b = [190, 55, 0, 0]

c = [-23, -17]

result = linprog(c, A, b, method='simplex').x
sum = 0
for i in range(numpy.size(c)):
     sum += -c[i]*result[i]
numpy.set_printoptions(suppress=True)

print("Zadanie 1\n"
      "Rozwiązania: ", result,
      "\nWartość funkcji celu: ", sum)

#zadanie 2
A = [[4, 3],
     [1, 1],
     [1, 0],
     [-1, 0],
     [0, -1]]

b = [190, 55, 47, 0, 0]

c = [-23, -17]

result = linprog(c, A, b, method='simplex').x
sum = 0
for i in range(numpy.size(c)):
     sum += -c[i]*result[i]
numpy.set_printoptions(suppress=True)

print("Zadanie 2\n"
      "Rozwiązania: ", result,
      "\nWartość funkcji celu: ", sum)

#zadanie 3
A = [[4, 3],
     [1, 1],
     [-1, 0],
     [-1, 0],
     [0, -1]]

b = [190, 55, -48, 0, 0]

c = [-23, -17]

result = linprog(c, A, b, method='simplex').x
sum = 0
for i in range(numpy.size(c)):
     sum += -c[i]*result[i]
numpy.set_printoptions(suppress=True)

print("Zadanie 3\n"
      "Rozwiązania: ", result,
      "\nWartość funkcji celu: ", sum)

#zadanie 4
A = [[4, 3],
     [1, 1],
     [1, 0],
     [0, 1],
     [-1, 0],
     [0, -1]]

b = [190, 55, 47, 0, 0, 0]

c = [-23, -17]

result = linprog(c, A, b, method='simplex').x
sum = 0
for i in range(numpy.size(c)):
     sum += -c[i]*result[i]
numpy.set_printoptions(suppress=True)

print("Zadanie 4\n"
      "Rozwiązania: ", result,
      "\nWartość funkcji celu: ", sum)

#zadanie 5
A = [[4, 3],
     [1, 1],
     [1, 0],
     [0, -1],
     [-1, 0],
     [0, -1]]

b = [190, 55, 47, -1, 0, 0]

c = [-23, -17]

result = linprog(c, A, b, method='simplex').x
sum = 0
for i in range(numpy.size(c)):
     sum += -c[i]*result[i]
numpy.set_printoptions(suppress=True)

print("Zadanie 5\n"
      "Rozwiązania: ", result,
      "\nWartość funkcji celu: ", sum)

#zadanie 6
A = [[4, 3],
     [1, 1],
     [1, 0],
     [0, -1],
     [1, 0],
     [-1, 0],
     [0, -1]]

b = [190, 55, 47, -1, 46, 0, 0]

c = [-23, -17]

result = linprog(c, A, b, method='simplex').x
sum = 0
for i in range(numpy.size(c)):
     sum += -c[i]*result[i]
numpy.set_printoptions(suppress=True)

print("Zadanie 6\n"
      "Rozwiązania: ", result,
      "\nWartość funkcji celu: ", sum)

#zadanie 7
A = [[4, 3],
     [1, 1],
     [1, 0],
     [0, -1],
     [-1, 0],
     [-1, 0],
     [0, -1]]

b = [190, 55, 47, -1, -47, 0, 0]

c = [-23, -17]

result = linprog(c, A, b, method='simplex').x
sum = 0
for i in range(numpy.size(c)):
     sum += -c[i]*result[i]
numpy.set_printoptions(suppress=True)

print("Zadanie 7\n"
      "Rozwiązania: ", result,
      "\nWartość funkcji celu: ", sum)