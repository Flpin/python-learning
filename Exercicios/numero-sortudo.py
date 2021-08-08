contador = 0
errado = 0
for i in range (18644, 33087):
    l = str(i)
    if "2" in l and "7" not in l:
        contador = contador + 1
    else:
        errado = errado + 1




print(f"São {contador} números sortudos")
print(f"São {errado} números sem sorte")       


#   if i in "2" and i not in "7":
