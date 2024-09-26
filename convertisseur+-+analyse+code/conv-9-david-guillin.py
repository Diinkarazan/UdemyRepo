UNITE_CM = "cm"
UNITE_POUCE = "inch"
resultat = ""
 
 
def menu_choix():
    choix_int = 0
    # 1 - Demander à l'utilisateur s'il souhaite convertir de "pouces vers cm" ou "cm vers pouces"
    choix_menu = input(f"""
        1 - convertir de "{UNITE_POUCE} vers {UNITE_CM}"
        2 - convertir de "{UNITE_CM} vers {UNITE_POUCE}"
        3 - sortir
    """)
    try:
        choix_int = int(choix_menu)
    except ValueError:
        print("ERREUR!!!!")
    else:
        if choix_int < 1 or choix_int > 3:
            print("ERREUR: Les valeurs doivent être comprise entre 1 et 3")
    return choix_int
 
 
# Boucler pour convertir plusieurs valeurs (en conservant toujours le même sens de conversion),
# et proposer une option pour sortir du programme.
choix = 0
while not choix == 3:
    choix = menu_choix()
    if choix == 1:
        # Demander à l'utilisateur s'il souhaite convertir de pouces vers cm
        valeur_str = input(f"Rentrer la valeur à convertir (de {UNITE_POUCE} en {UNITE_CM}) ?")
        try:
            valeur_float = round(float(valeur_str) * 2.54, 2)
            resultat = f"=> La valeur de {valeur_str} {UNITE_POUCE} vaut {valeur_float} en {UNITE_CM}"
            # 3 - Afficher la valeur convertie (et l'unité : cm ou pouces)
            print(resultat)
        except ValueError:
            print("Seul, les nombres sont acceptés!")
    elif choix == 2:
        # Demander à l'utilisateur s'il souhaite convertir de cm vers pouces
        valeur_str = input(f"Rentrer la valeur à convertir (de {UNITE_CM} en {UNITE_POUCE}) ?")
        try:
            valeur_int = round(int(valeur_str) * 0.394, 2)
            resultat = f"=> La valeur de {valeur_str} {UNITE_CM} vaut {valeur_int} en {UNITE_POUCE}"
            # 3 - Afficher la valeur convertie (et l'unité : cm ou pouces)
            print(resultat)
        except ValueError:
            print("Seul, les nombres sont acceptés!")