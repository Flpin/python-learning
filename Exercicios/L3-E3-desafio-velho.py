"""Verifique se um inteiro positivo n é primo."""

n = int(input("numero: ")) #15
import timeit

start = timeit.default_timer()

#Your statements here

stop = timeit.default_timer()

print('Time: ', stop - start)
i = 1
contador = 0

i = 1
contador = 0

while i < n:
    if n % i == 0:
        contador = contador + 1

    i = i + 1

if contador <= 2:   
    print("é primo")



else:
    print("não é primo")



