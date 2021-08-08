n = int(input("numero: ")) 
import timeit

start = timeit.default_timer()

#Your statements here

stop = timeit.default_timer()

print('Time: ', stop - start)
i = 2
if n == 1:
    print("1 é sempre primo")
    
while n >= i: 
    if n % i == 0 and n != i:
        print("Não é primo")
        break
    if n == i:
        print("É primo")

    i = i + 1






























