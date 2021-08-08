def card_hide(card):
    novo_card = ""
    for i in range(len(card) - 4):
        novo_card += "*"
    return novo_card + card[-4:]

print(card_hide("35123413355523"))
##
##def card_hide(card):
##    return ("*" * (len(card) - 4)) + card[-4:]
##print(card_hide("1234123456785678"))
