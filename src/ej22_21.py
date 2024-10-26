#Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.
from mi_libreria import comprobar_num
# comprueba si el monto es negativo (si lo es bucle) y si es 0 (retorna None, para después en el while del main)
def comprobar_monto(num):
    num = comprobar_num(num)
    if num == 0:
        num = None
        return num
    if num < 0:
        while num < 0: 
            print ("*Error*")
            num = float(comprobar_num(input("Introduce un monto válido: ").replace(" ","")))
    return num
def ingreso_monto():
    monto = input("Introduce un monto (0 para parar): ").replace(" ","")
    return comprobar_monto(monto)

def main():
    print("Introduce los montos:")
    monto = ingreso_monto()
    total = 0
    # cuando monto sea 0, es decir, None termina los ingresos de montos. 
    while monto is not None:
        total += monto
        monto = ingreso_monto()
    
    # Si total es mayor a 1000 se aplica un 10% de descuento
    if total > 1000:
        total -= total *0.1
    print (f"El total a pagar es {total}")
    
if __name__ == "__main__":
    main()