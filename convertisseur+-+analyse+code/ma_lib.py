# 1 pouce = 2.54 cm
# 1 cm = 0.394 pouces
 
 
def inch_into_cm(value):
    """Conversion de pouces vers centimetres"""
    return value * 2.54
 
def cm_into_inch(value):
    """Conversion de centimetres vers pouces"""
    return int(value*0.394)
 
def conversion(converter, unit):
    value = float(input(f"La valeur a convertir en {unit}: "))
    return str(converter(value)) + unit
 
 
def main():
    print("1-pouces vers cm")
    print("2-cm vers pouces")
    user_choice = int(input(": "))
    if user_choice == 1:
        print(conversion(inch_into_cm, "cm"))
    elif user_choice == 2:
        print(conversion(cm_into_inch, "pouces"))
    else:
        print("Cette option n\'existe pas !")
        

# es-ce que on a lancé ce programme python ou est-ce qu'on l'a importé
if __name__ == "__main__":
    main()