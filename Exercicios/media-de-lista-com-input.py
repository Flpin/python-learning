"""Média de lista com input"""

notas = []
x = 1

while x <= 4:
    notas.append(float(input("Digite qual nota gostaria de adicionar: ")))    
    x = x + 1

soma = x = 0

while x <= 3:
    soma = soma + notas[x]
    x = x + 1

media = soma / (len(notas))

print(f"A média das notas: {[notas]} é: {media}")
