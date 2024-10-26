#Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más de una, mostrar la primera) y cuántas palabras había. Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.

def pedir_frase():
    print ("Introduce una frase:" , end=" ")
    frase = input ("").strip() # elimina espacios al inicio y al final
    return frase


#cuenta el número de palabras
def contar_num_palabras(frase):
    # añado un espacio para que cuente a la última palabra (ya que para que cuente la palabra necesita un espacio detras, si no, no ejecuta el if)
    frase += " "
    # variable vacía para cada palabra
    palabra = ""
    #contador de palabras
    contador = 0
    #recorre la frase
    for i in frase:
        # Si i es un espacio no lo añade a la palabra. En caso de que la longitud de palabra sea mayor a 0(eso quiere decir que 'palabra' es una palabra) suma 1 al contador y restea 'palabra'. Si la longitud llegase a ser 0 es que era un espacio (ya que como no se puede añadir a 'palabra' la longitud de 'palabra' es 0) 
        if i == " ":
            if len(palabra) > 0:
                contador += 1
                palabra = ""
        else: # Si i no es un espacio lo añade a la palabra
            palabra += i
    return contador

def encontrar_palabra_mas_larga(frase):
    # añado un espacio para que cuente a la última palabra (ya que para que cuente la palabra necesita un espacio detras, si no, no ejecuta el if)
    frase += " "
     # variable vacía para cada palabra
    palabra=""
    #variable vacia para la palabra más larga
    mayor = ""
    for i in frase:
        # Si i es un espacio no lo añade a la palabra. En caso de que la longitud de 'palabra' sea mayor a la palabra más larga, se vuelve la más larga y resetea 'palabra'. 
        if i == " ": 
            if len(palabra) > len(mayor):
                mayor = palabra
            palabra = ""
        else: # Si i no es un espacio lo añade a la palabra
            palabra += i
    return mayor                
            
            
    
        
        
def main():
    frase = pedir_frase()
    num_palabras = contar_num_palabras(frase)
    mas_larga = encontrar_palabra_mas_larga(frase)
    print (f"Hay {num_palabras} palabras y la más larga es {mas_larga}")
    
if __name__ == "__main__":
    main()