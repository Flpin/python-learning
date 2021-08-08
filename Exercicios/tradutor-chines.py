def chines(msg):
  cadaLetra = ""
  for letra in msg:
      cadaLetra = cadaLetra + chr(ord(letra) + 30000)
  return cadaLetra


resultado = chines(input("Digite a palavra: "))
print(resultado)
