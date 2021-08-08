"""Faça um Programa que leia três números e mostre o maior deles."""

def maiorNumeroEntre3(a,b,c):   
    maior = n1

    if b > maior:
        maior = b
    
    if c > maior:
        maior = c

    return maior

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

a = maiorNumeroEntre3(n1,n2,n3)
print(f"O maior número é {a}")
