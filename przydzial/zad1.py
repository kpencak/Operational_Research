import numpy

warsztaty = numpy.array([[5, 7, 8, 7],
                        [6, 4, 7, 6],
                        [7, 5, 6, 5],
                        [4, 3, 5, 9]])

marki = ["Ford", "Volkswagen", "Toyota", "Fiat"]

# STEP 1: Write zero in each row
columns = numpy.size(warsztaty, 1)
rows = numpy.size(warsztaty, 0)

for i in range(rows):
    minimum_row = numpy.min(warsztaty[i])
    for j in range(columns):
        warsztaty[i][j] = warsztaty[i][j] - minimum_row
print("Macierz po usunieciu elementu w wierszach")
print(warsztaty)

warsztatyT = warsztaty.transpose()
# Check if there is zero in each column as well
for i in range(rows):
    minimum_row = numpy.min(warsztatyT[i])
    for j in range(columns):
        warsztatyT[i][j] = warsztatyT[i][j] - minimum_row

warsztaty = warsztatyT.transpose()
print("Macierz po usunięciu elementu w kolumnach")
print(warsztaty)

# STEP 2: cross out lines
lines = 3
print("Liczba linii do wykreślenia: ", lines)

if lines < rows:
    print("Przejście do kroku 4")
else:
    print("Przejście do kroku 3, rozwiązanie optymalne")

# STEP 3: optimize (skipped)

# STEP 4: revise
minimum_array = 1
print("Minimum macierzy: ", minimum_array)
for i in range(rows):
    if i == 1 or i == 3:
        for j in range(columns):
            if j == 0 or j == 2 or j == 3:
                warsztaty[i][j] = warsztaty[i][j] - minimum_array
    else:
        for j in range(columns):
            if j == 1:
                warsztaty[i][j] = warsztaty[i][j] + minimum_array

print("Macierz po przekształceniach kroku 4")
print(warsztaty)

# STEP 2: cross out lines
lines = 4
print("Liczba linii do wykreślenia: ", lines)

if lines < rows:
    print("Przejście do kroku 4")
else:
    print("Przejście do kroku 3, rozwiązanie optymalne")

