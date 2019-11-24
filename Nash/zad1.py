import numpy

A = numpy.array([[20, -150, -250],
                 [150, -80, -100],
                 [250, 100, 40]])


def minimax_row(matrix):
    minimax = []
    for i in matrix:
        minimax.append(i.min())

    minimax = numpy.asarray(minimax)
    return minimax.max()


def minimax_column(matrix):
    size = numpy.shape(matrix)[0]
    minimax = []
    for i in range(size):
        column = matrix[:, i]
        minimax.append(column.max())

    minimax = numpy.asarray(minimax)
    return minimax.min()


def is_nash_balance(matrix, min_row, min_col):
    size = numpy.shape(matrix)[0]
    if min_row == min_col:
        for i in range(size):
            for j in range(size):
                if matrix[i][j] == min_row:
                    print("Równowaga zachodzi dla decyzji: A{0} B{1}".format(i+1, j+1))
    else:
        print("Równowaga nie zachodzi dla żadnej z decyzji.")


player1 = minimax_row(A)
player2 = minimax_column(A)
is_nash_balance(A, player1, player2)