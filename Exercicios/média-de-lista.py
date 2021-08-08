"""Média de uma lista de notas"""

notas = [6, 7, 8, 9, 10]
x = 0
soma = 0

while x < len(notas):
    soma = soma + notas[x]
    x = x + 1
media = soma / len(notas)

print(f"A média dos números {notas} é: {media}") 
