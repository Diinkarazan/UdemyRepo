inch_to_cm = 2.54
cm_to_inch = 0.394
 
def convert_inch_to_cm(number):
    return f"{number} pouce(s) = {number*inch_to_cm} cm"
 
def convert_cm_to_inch(number):
    return f"{number} cm = {number*cm_to_inch} pouce(s)"
 
while True:
    convert_choice = input("Choisir une conversion à effectuer. Tapez 1, 2 ou 3.\n1: pouces vers cm\n2: cm vers pouces\n3: Quitter le programme\n>")
    try:
        int_convert_choice = int(convert_choice)
    except:
        print("Entrée invalide, veuillez réessayer.\n")
 
    if int_convert_choice == 3:
        quit()
 
    value_choosen = input("Entrez la valeur et l'unité à convertir (cm ou pouce(s)):")
    splited_value = value_choosen.split()
    unite = splited_value[-1]
    valeur_a_convertir = splited_value[0]
 
    if not (unite == "cm" or unite == "pouce" or unite == "pouces"):
        print("Unité de mesure incorrecte.")
    else:
        try:
            f_convert_value = float(valeur_a_convertir)
        except:
            print("Entrée invalide, veuillez réessayer.\n")
            continue
 
        if int_convert_choice == 1:
            print(convert_inch_to_cm(f_convert_value))
        elif int_convert_choice == 2:
            print(convert_cm_to_inch(f_convert_value))