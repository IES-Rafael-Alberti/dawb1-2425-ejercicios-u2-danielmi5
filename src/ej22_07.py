#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
def tabla_multiplicar():
    for num in range (1,11):
        print(f"Tabla del {num}")
        for i in range(1,11):
            print(f"{num}x{i} =",num*i)
        print("")
    
def main():
    print ("Tabla de multiplicar del 1 al 10")
    tabla_multiplicar()
    
if __name__ == "__main__":
    main()

