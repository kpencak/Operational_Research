import numpy
from numpy import linalg as lin

bag = [[  1,   5, 3],
       [1/5,   1, 3],
       [1/3, 1/3, 1]]

passengers = [[  1,   1, 7],
              [  1,   1, 7],
              [1/7, 1/7, 1]]

cena_sam = [[  1, 1/5, 3],
            [  5,   1, 9],
            [1/3, 1/9, 1]]

paliwo = [[  1, 4, 1/5],
          [1/4, 1, 1/8],
          [  5, 8,   1]]

safety = [[  1, 4, 1/5],
          [1/4, 1, 1/7],
          [  5, 7,   1]]

ceny = [[1, 1/5],
        [5,   1]]

pojemnosc = [[1, 1/3],
             [3,   1]]

C = [[  1, 1/7, 3],
     [  7,   1, 9],
     [1/3, 1/9, 1]]

#ranking podkategorii cen
w_sam, v_sam = lin.eig(cena_sam)
w_pal, v_pal = lin.eig(paliwo)
w_ceny, v_ceny = lin.eig(ceny)
index_sam = numpy.argmax(w_sam)
index_pal = numpy.argmax(w_pal)
index_ceny = numpy.argmax(w_ceny)

wektor_sam = lin.eig(cena_sam)[1][:, index_sam]
sum_sam = numpy.sum(numpy.abs(wektor_sam))
wektor_sam = numpy.abs(wektor_sam)/sum_sam

wektor_pal = lin.eig(paliwo)[1][:, index_pal]
sum_pal = numpy.sum(numpy.abs(wektor_pal))
wektor_pal = numpy.abs(wektor_pal)/sum_pal

wektor_ceny = lin.eig(ceny)[1][:, index_ceny]
sum_ceny = numpy.sum(numpy.abs(wektor_ceny))
wektor_ceny = numpy.abs(wektor_ceny)/sum_ceny

ceny_matrix = numpy.column_stack((wektor_sam, wektor_pal))
ceny_result = ceny_matrix @ wektor_ceny

#ranking podkategorii pojemnosci
w_bag, v_bag = lin.eig(bag)
w_pas, v_pas = lin.eig(passengers)
w_poj, v_poj = lin.eig(pojemnosc)
index_bag = numpy.argmax(w_bag)
index_pas = numpy.argmax(w_pas)
index_poj = numpy.argmax(w_poj)

wektor_bag = lin.eig(bag)[1][:, index_bag]
sum_bag = numpy.sum(numpy.abs(wektor_bag))
wektor_bag = numpy.abs(wektor_bag)/sum_bag

wektor_pas = lin.eig(passengers)[1][:, index_pas]
sum_pas = numpy.sum(numpy.abs(wektor_pas))
wektor_pas = numpy.abs(wektor_pas)/sum_pas

wektor_poj = lin.eig(pojemnosc)[1][:, index_poj]
sum_poj = numpy.sum(numpy.abs(wektor_poj))
wektor_poj = numpy.abs(wektor_poj)/sum_poj

poj_matrix = numpy.column_stack((wektor_bag, wektor_pas))
poj_result = poj_matrix @ wektor_poj

#ranking kategorii
w_safe, v_safe = lin.eig(safety)
w_C, v_C = lin.eig(C)
index_safe = numpy.argmax(w_safe)
index_C = numpy.argmax(w_C)

wektor_safe = lin.eig(safety)[1][:, index_safe]
sum_safe = numpy.sum(numpy.abs(wektor_safe))
wektor_safe = numpy.abs(wektor_safe)/sum_safe

wektor_C = lin.eig(C)[1][:, index_C]
sum_C = numpy.sum(numpy.abs(wektor_C))
wektor_C = numpy.abs(wektor_C)/sum_C

vector_matrix = numpy.column_stack((ceny_result, poj_result, wektor_safe))
result = vector_matrix @ wektor_C
print(numpy.real(result))