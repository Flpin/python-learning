def calculator(num1, operator, num2):
    if operator == "+":
        resultado = (num1 + num2)
    elif operator == "-":
        resultado = (num1 - num2)
    elif operator == "/":
        if num2 == 0:
            return("Can't divide by 0!")
        else:
            resultado = (num1 / num2)
    else:
        resultado = (num1 * num2)
    return (resultado)

print(calculator(2,"*",2))
print(calculator(2, "+", 2))
print(calculator(2, "*", 2))
print(calculator(4, "/", 0))                    

##def calculator2(num1, operator,num2):
##    return num1 + num2 if operator == "+" else 0
##
##print(calculator2(4,"+",2))
##
##
