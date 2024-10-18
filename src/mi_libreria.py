def comprobar_num(num: str) -> int:
    if num.isdigit():
        return int(num)
    else:
        while not num.isdigit():
            if num.startswith("-"):
                num = num.replace("-","",1)
                if num.isdigit():
                    num = "-" + num
                    return int(num)
            print("ERROR: Debes introducir un número: ")
            num = input("").replace(" ","")
    return int(num)