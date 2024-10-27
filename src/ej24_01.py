"""Ordena la lista:

Args:
lista_ordenada(bool): para controlar el bucle while (True: Si está ordenada) (False: si no lo está)
i (int): Número en ese momento
posicion_i (int): posición de i
lista (list): La lista de números del main()

return:
lista (list): Lista ya ordenada
"""
def ordenar_lista(lista):
    lista_ordenada = False
    while lista_ordenada == False:
        posicion_i = 0
        #recorre la lista
        for i in lista:
            # si i es el último número no hace nada
            if i == lista[len(lista)-1]: 
                pass
            else: # de lo contrario comprueba si es mayor al próximo
                if lista[posicion_i] > lista[posicion_i+1]: # si lo es intercambian posiciones
                    lista[posicion_i] = lista[posicion_i+1]
                    lista[posicion_i+1] = i
                else: #si no lo es no hace nada
                    pass
            # suma 1 a posicion_i
            posicion_i+=1
        # si al comprobar la lista, está ordenada da True a lista_ordenada
        if comprobar_lista_ordenada(lista) == True:
            lista_ordenada = True
        else: # si no lo está, vuelve a repetir el bucle.
            pass
    # Cuando esté ordenada, retorna la lista.
    return lista

""" Comprueba si la lista está ordenada:

Args:
i (int): Posición en la lista
lista (list): La lista de números actualizada (en ese momento) del bucle de ordenar_lista()

Return:
booleano: True: si la lista está ordenada | False: si la lista no está ordenada
"""     
            
def comprobar_lista_ordenada(lista):
    # recorre desde la posición 0 hasta la posición final de la lista
    for i in range(0,len(lista)):
        # si el número (en ese momento) es el último, no hace nada
        if lista[i] == lista[len(lista)-1]: 
            pass
        else: # De lo contrario
            #si el numero llegase a ser mayor al próximo, retorna False porque no estaría ordenada.
            if lista[i] > lista[i+1]:
                return False
    #Si sale del bucle es que la lista está ordenada y retorna True
    return True
   
                
                


def main():
   a = [8, 3, 1, 19, 14]
   print(a)
   lista_ordenada = ordenar_lista(a)
   print (f"Lista ordenada: {lista_ordenada}")
if __name__ == "__main__":
    main()