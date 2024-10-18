def introducir_num(msj) -> bool:
    num = None
    try:
        num = float(input(msj))
    except ValueError:
        print ("*ERROR* número invalido!")
    return num
def main():
    num = introducir_num("Introduce un número: ")
    while (num is None):
        num = input("Introduce un número: ")
    

if __name__ == "__main__":
    main()
