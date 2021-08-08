"""Média de lista com input"""

notas = []
z = 0
soma = 0

while True:
    x = float(input("Digite qual nota gostaria de adicionar(Digite 0 quando quiser calcular a média das notas: "))
    notas.append(x)
    if x == 0:
        break

for i in range(len(notas)-1):
    soma = soma + notas[z]
    z = z + 1
media = soma / (len(notas)-1)

print(f"A média das notas: {[notas]}, é {media}")
    
