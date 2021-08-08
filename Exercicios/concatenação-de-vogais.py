"""Concatenação de strings - trocar vogais por (*) """

x = 0
troca = ""

palavra = input("Digite a palavra para a troca de vogais por *: ")

while x < len(palavra):
    if palavra[x] in 'aeiou':
        troca = troca + "*"
    else:
        troca = troca + palavra[x]
    x = x + 1
print(f"A palavra ficou: {troca}.")
    
