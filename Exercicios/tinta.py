def apaga(string, n):
    novaPalavra = ""
    for (indice) in range (len(string)): #s = gremio , n  = 2
        if indice != (n):
            novaPalavra += string[indice]
    return novaPalavra

print(apaga("gremio", 4))



