def numerosSortudos(a):
    a = str(a)
    if "2" in a and "7" not in a:
        return True

    return False


soma = 0
azar = 0

n1 = int(input("Digite o 1 número: "))
n2 = int(input("Digite o 2 número: "))

for i in range(n1, n2):
    if numerosSortudos(i) == True:
        soma += 1
    

print(f"Os números sortudos são {soma}")
print(f"Os números azarados são {(n2 - n1) - soma}")
