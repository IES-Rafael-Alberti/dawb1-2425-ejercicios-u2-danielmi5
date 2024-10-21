def comprobar_num(msj:str) -> bool:
    num = float(input(msj))
    return num
def main():
   try:
       num = comprobar_num("Introdce nu número: ")
       divisor = comprobar_num("Introduce número: ")
       resultado = num / divisor
       print ("El resultado es:", resultado)
       return 0
    except ValueError:
        return 0
    except ZeroDivisionError:
        pass
    except: # except sin nada, lo hace pero no sabes pq
      return 0
       
if __name__ == "__main__":
    main()

def comprobar_num(num):        
    if num.isdigit() == True:
        #Aprovecho para comprobar si el numero es positivo o negativo
        if int(num) < 0:
            while float(num) < 0:
                print ("ERROR")
                num = (input("Debes introducir un número (positivo): ").replace(" ",""))
        if float(num) >= 0:
            return float(num)      
        return float(num)  
    else:
        while num.isdigit() == False:
        print ("ERROR")
        num = input("Debes introducir un número (positivo): ").replace(" ","")
        if num.isdigit() == True:
            return int(num)




