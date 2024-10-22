#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
##Ingredientes vegetarianos: Pimiento y tofu.
##Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

def comprobar_respuesta(entrada: str):
    # compruebo si es una afirmación o negación, si no lo es, bucle hasta que sí sea
    afirmacion = ["si","sí"]
    negacion = "no"
    respuesta = None
    if not entrada.lower() in afirmacion and entrada.lower() != negacion:
        while respuesta is None:
            entrada = input("Introduce una respuesta válida: ").replace(" ","")
            if entrada.lower() in afirmacion or entrada.lower() == negacion:
                respuesta = True
        
    return entrada

def introducir_menu(entrada: str):
    entrada = comprobar_respuesta(entrada).lower()
    
    if entrada in ["si","sí"]:
        print("""Menú vegetariano, ingredientes disponibles:
Mozzarella, tomate y un ingrediente a tu elección (Pimiento o tofu).
""")
    
    else:
        print("""Menú no vegetariano, ingredientes disponibles:
Mozzarella, tomate y un ingrediente a tu elección (Peperoni, jamón o salmón).
""")
        
def comprobar_elección(eleccion: str, ingredientes_vegetarianos: list, ingredientes_no_vegetarianos: list):
    # compruebo si la elección esté dentro del rango, si no lo es, bucle hasta que sí sea
    
    # la eleción en minusculas por si añade mayúsculas
    eleccion = eleccion.lower()
    respuesta = None
    if not eleccion in ingredientes_vegetarianos and not eleccion in ingredientes_no_vegetarianos:
        while respuesta is None:
            eleccion = (input("Introduce una respuesta válida: ").replace(" ","")).lower()
            if eleccion in ingredientes_vegetarianos or eleccion in ingredientes_no_vegetarianos:
                respuesta = True   
    # Esto es para que, en caso de no poner la tilde, remplazar la o por la o con tilde (Para que en el print final salga con tilde)
    if eleccion == "jamon" or eleccion == "salmon":
        eleccion = eleccion.replace("o","ó")
    return eleccion

def main():
    ingredientes_vegetarianos = ["pimiento", "tofu"]; ingredientes_no_vegetarianos = ["peperoni", "jamón", "jamon", "salmón", "salmon"]
    print("¿Quieres una pizza vegetariana?")
    entrada = input("").replace(" ", "")
    introducir_menu(entrada)
    
    eleccion = input("Elige ingrediente: ").replace(" ","")
    eleccion = comprobar_elección(eleccion, ingredientes_vegetarianos, ingredientes_no_vegetarianos)
    if eleccion in ingredientes_vegetarianos:
        print(f"La pizza es vegetariana y los ingredientes son: Mozzarella, tomate y {eleccion}.")
    elif eleccion in ingredientes_no_vegetarianos:
         print(f"La pizza no es vegetariana y los ingredientes son: Mozzarella, tomate y {eleccion}.")
if __name__ == "__main__":
    main()