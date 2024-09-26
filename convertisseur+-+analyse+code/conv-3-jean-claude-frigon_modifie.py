def display_menu():
    print("******************************************")
    print("*        Utilitaire de conversion        *")
    print("******************************************")
    print("* 1 - Convertion pouces -> cm            *")
    print("* 2 - Convertion cm -> pouces            *")
    print("* 3 - Quitter                            *")
    print("******************************************")
    return input("Votre choix? ")
 
 
VALEUR_CONVERSION_POUCES_VERS_CM = 2.54
 
while True:

    choix = display_menu()
 
    # sortie du programme
    if choix == "3":
        break
 
    val_str = input("Quelle est la valeur à convertir?")
 
    try:
        val_flt = float(val_str)
    except ValueError:
        print("Erreur: Le texte entré doit être numérique incluant ou non le '.'")
        continue
 
    if choix == "1":
        resultat = val_flt * VALEUR_CONVERSION_POUCES_VERS_CM
        print(f"La valeur convertie de {val_flt} pouces est {resultat}cm.")
        print()
        input("Appuyer sur Entrer pour continuer.")
    elif choix == "2":
        resultat = val_flt / VALEUR_CONVERSION_POUCES_VERS_CM
        print(f"La valeur convertie de {val_flt}cm est {resultat} pouces.")
        print()
        input("Appuyer sur Entrer pour continuer.")
    else:
        print("Les choix sont 1, 2 ou 3.  Veuillez sélectionner un choix valide.")