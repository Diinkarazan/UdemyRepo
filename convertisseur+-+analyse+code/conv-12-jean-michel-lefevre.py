INCH_VALUE = 2.54
CM_VALUE = 0.394
continuer = True
def CmToInch ():
    value_to_convert_int = 0
    while value_to_convert_int == 0 :
        value_to_convert_str = input("Combien de Cm souhaitez vous convertir en Pouce : ")
        try:
            value_to_convert_int = int(value_to_convert_str)
        except:
            print("Vous devez entrer un nombre entier. ")
    result = value_to_convert_int * CM_VALUE
    print(f"{value_to_convert_int} Cm est egal a {result} Pouce")
 
 
def InchToCm ():
    value_to_convert_int = 0
    while value_to_convert_int == 0 :
        value_to_convert_str = input("Combien de Pouce souhaitez vous convertir en Cm : ")
        try:
            value_to_convert_int = int(value_to_convert_str)
        except:
            print("Vous devez entrer un nombre entier. ")
    result = value_to_convert_int * INCH_VALUE
    print(f"{value_to_convert_int} Pouce est egal a {result} Cm")
 
while continuer:
    print()
    print("pour convertir des centimetres en pouce tapez '1' ou 'cm'")
    print("pour convertir des pouces en centimetres tapez '2' ou 'inch'")
    print()
 
    user_unite = input("Votre unité : ")
    if user_unite == "1" or user_unite =="cm":
        CmToInch()
    elif user_unite == "2" or user_unite =="inch":
        InchToCm()
    else:
        print("Ce choix n'existe pas")
    print()
    user_unite=input("Tapez 'q' ou 'quit' pour quitter ou autre pour continuer ")
    if user_unite == "q" or user_unite == "quit":
        continuer = False
    else:
        continuer