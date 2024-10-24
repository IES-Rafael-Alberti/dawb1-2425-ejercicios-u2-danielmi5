numero = 12
fila = ""

for i in range (2, numero +1, 2):
    for i in range (i, -2, -2):
        if i == 2:
            fila += str(i)
            break
        else:
            fila += str(i) + " "
    fila += "\n"
print (fila)    
