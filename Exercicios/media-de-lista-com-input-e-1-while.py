"""Média de lista com input"""

notas = []
x = 0
soma = 0

while x <= 3:
    notas.append(float(input("Digite qual nota gostaria de adicionar: ")))    
    soma = soma + notas[x]
    x = x + 1

media = soma / (len(notas))

print(f"A média das notas: {[notas]} é: {media}")


