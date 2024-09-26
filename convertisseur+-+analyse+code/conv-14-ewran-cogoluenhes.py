INCH_TO_CM = 2.54
CM_TO_INCH = 0.394
 
print("Bonjour et bienvenue dans le convertisseur cm => pouces")
print()
 
def conversion(sens, user_input):
    if sens == 2:
        calcul = CM_TO_INCH * user_input
    else:
        calcul = INCH_TO_CM * user_input
    return round(calcul, 2)
        
def unit_confirmation():
    print()
    confirm_unit = input("Veuillez confirmer l'unité de la valeur saisie (pouces ou cm): ")
    global str_user_unit
    global converted_unit
 
    if user_choice == 1:
        str_user_unit = "pouces"
        converted_unit = "cm"
    elif user_choice == 2:
        str_user_unit = "cm"
        converted_unit = "pouces"
 
    while not confirm_unit == str_user_unit:
        
        print()
        confirm_unit = input("Vous n'avez pas fait ce choix d'unité au départ, veuillez taper à nouveau ou relancez le programme: ")
 
 
 
user_choice = 0
while not (user_choice == 1 or user_choice == 2):
    print()
    user_choice = input("Veuillez indiquer le sens de conversion: 1 pour pouces => cm , 2 pour cm => pouces: ")
    
    try:
        user_choice = int(user_choice)
        if not (user_choice == 1 or user_choice == 2):
            print()
            print("Entrer 1 ou 2, c'est pas dur quand même !")
 
    except:
        print()
        print("EREUR: Veuillez répondre 1 ou 2")
 
user_input = float(input("Entrez la valeur à convertir: "))
program_continue = 1
 
while program_continue == 1:
    print()
    unit_confirmation()
 
 
    print()
    print("Les résultat est: " + str(user_input) + " " + str_user_unit + " = " + str(conversion(user_choice, user_input)) + " " + converted_unit)
    new_value = input("Pour continuer, saisissez une nouvelle valeur ou appuyez sur entrée pour quiter: ")
    if not new_value == "":
        user_input = int(new_value)
        program_continue = 1
    else:
        program_continue = 0
        print("Fin du programme")