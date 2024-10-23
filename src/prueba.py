num = input("Introduce")
contador = 0
terminar = False
eco = ""

while num.lower() != "salir":
    eco += num + " "
    print(eco)
    num = input("Introduce otro")
    