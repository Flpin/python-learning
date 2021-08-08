"""Verificar se a palavra é palindrome"""

palavra = input("Digite a palavra para verificar se é palindrome: ")

if palavra[::-1] == palavra:
    print(f"A palavra {palavra} é palindrome.")
else:
    print(f"A palavra {palavra} não é palindrome pois fica {palavra[::-1]} ao contrário.")
