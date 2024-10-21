#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
##Ingredientes vegetarianos: Pimiento y tofu.
##Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

Ingredientes_vegetarianos = ["pimiento", "tofu"]; Ingredientes_no_vegetarianos = ["peperoni", "jamón", "jamon", "salmón", "salmon"]
Ingredientes_pizza = ["Mozarella", "tomate"]

def comprobar_respuesta(entrada: str) -> bool:
    afirmacion = ["si","sí"]
    negacion = "no"
    respuesta = None
    if not entrada.lower() in afirmacion and entrada.lower() != negacion:
        while respuesta is None:
            entrada = input("Introduce una respuesta válida: ")
            if entrada.lower() in afirmacion or entrada.lower() == negacion:
                respuesta = True
        
    return entrada

def intoducir_menu(entrada):
    comprobar_respuesta(entrada)
    if entrada in ["si","sí"]:
        print("""Menú vegetariano, ingredientes disponibles:
Mozarrella , Tomate y un ingrediente a tu elección (Pimiento o tofu)
""")
    
    else:
        print("""Menú no vegetariano, ingredientes disponibles:
Mozarrella, tomate y un ingrediente a tu elección (Peperoni, jamón o salmón)
""")
        
def comprobar_elección(eleccion):
    respuesta = None
    if not eleccion.lower() in Ingredientes_vegetarianos and not eleccion.lower() in Ingredientes_no_vegetarianos:
        while respuesta is None:
            eleccion = input("Introduce una respuesta válida: ")
            if eleccion.lower() in Ingredientes_vegetarianos or eleccion.lower() in Ingredientes_no_vegetarianos:
                respuesta = True    
    return eleccion

def main():
    print("¿Quieres una pizza vegetariana?")
    entrada = input("").replace(" ", "")
    intoducir_menu(entrada)
    eleccion = comprobar_elección(input("Elige ingrediente: ").replace(" ",""))
    print("Los ingredientes son: Mozarella, tomate y {eleccion} .")
        
if __name__ == "__main__":
    main()