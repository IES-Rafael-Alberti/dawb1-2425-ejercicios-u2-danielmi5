#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
# imprime la tabal de multiplicar de cada número hasta 10
def tabla_multiplicar():
    # recorre desde 1 hasta 10
    for num in range (1,11):
        print(f"Tabla del {num}")
        # recorre desde 1 hasta 10 e imprime cada multiplicación con el resultado
        for i in range(1,11):
            print(f"{num}x{i} =",num*i)
        print("")
    
def main():
    print ("Tabla de multiplicar del 1 al 10")
    tabla_multiplicar()
    
if __name__ == "__main__":
    main()

