#Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). Finalmente, informar cuántas líneas completas se ingresaron.

def pedir_libro():
    print ("Libro:",end=" ") # para que el input esté detras
    libro = input("").strip() #elimina los espacios en blanco al inicio y al final
    return libro

# cuando introduzca * devuelve None y termina el bucle del main
def comprobar_libro(libro):
    if libro == "*":
        return None
    else: 
        return libro

#recorre libro y comprueba si es digito, si lo es, suma 1 al contador. Retorna el número de dígitos de ese libro
def contar_digitos_libro(libro):
    contador_digitos = 0
    for i in libro:
        if i.isdigit():
            contador_digitos += 1
        else: 
            continue
    return contador_digitos
    


def main():
    libro = pedir_libro()
    contador_linea = 0
    contador_digitos_linea = 0
    # Mientras que no salga * ejecuta el bucle
    while comprobar_libro(libro) is not None:
        #Suma todos los numeros de dígitos por libro hasta que finalice la línea en un contador, cuando esto ocurre se resetea el contador
        contador_digitos_linea += contar_digitos_libro(libro)
        if libro == "/":
            # cuando finaliza la línea, suma 1 al contador de líneas
            contador_linea += 1
            print (f"Línea completa. Aparecen {contador_digitos_linea} dígitos numéricos")
            contador_digitos_linea = 0
        # Al final del bucle vuelve a pedir otro libro
        libro = pedir_libro()
    print (f"Fin. Se leyeron {contador_linea} líneas completas.")
    
    
if __name__ == "__main__":
    main()