"""
Write a function that moves all elements of one type to the end of the list.
Examples
move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# Move all the 1s to the end of the array.
move_to_end([7, 8, 9, 1, 2, 3, 4], 9) ➞ [7, 8, 1, 2, 3, 4, 9]
# move_to_end(["a", "a", "a", "b"], "a") ➞ ["b", "a", "a", "a"]
"""

def move_to_end_flp(lista, elemento):
    x = 0
    z = 0
    listaNova = []
    for i in lista: # 1, 3
        if i != elemento:  
            listaNova.append(i)
        if i == elemento: 
            x = x + 1 # x = 1
    
    while z < x: # 0 < 1
        listaNova.append(elemento) # lista = [1,3,4,1]
        z = z + 1
    return listaNova

print(move_to_end_flp([3,4,5,6,7,8,9,],))
