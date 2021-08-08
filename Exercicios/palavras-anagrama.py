def valorDaString(palavra):
    soma = 0
    for letra in (palavra):
        cadaLetra = ord(letra) 
        soma = soma + cadaLetra
    return (soma)


palavra1, palavra2 = input("Digite duas palavras para saber se são anagramas: ").split(",")

a = valorDaString(palavra1)
b = valorDaString(palavra2)

if a == b:
    print(f"As palavras {palavra1} e {palavra2} são anagramas.")
else:
    print(f"As palavras {palavra1} e {palavra2} não são anagramas.")


