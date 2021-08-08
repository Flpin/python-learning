def int_to_NumStr(num): #65
    a = ""
    while num > 9: #65 > 9 
        a = chr(num % 10 + 48) + a # a = "5"
        num = num // 10 # num = 6
    a = chr(num + 48) + a
    return (a)

n = int(input("numero: "))
print(numStr_to_int(n))

print(type(numStr_to_int(n)))




