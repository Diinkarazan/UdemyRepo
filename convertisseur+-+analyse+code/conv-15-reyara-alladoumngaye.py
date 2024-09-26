print("**** CONVERSION DES CENTIMETRES EN POUCES ET DES POUCES EN CENTIMETRES ****")
print()
choix = "0"
while choix not in range(0, 2):
    choix = input("Pour convertir, taper 0 pour centimètres en pouces,1 pour pouces en centimètres ou RC pour sortir.")
    if str(choix) == "":
        print("Fin")
        break
    if choix == "0":
        test = True
        while test == True:
            x = input("Enter votre nombre en centimètres: ")
            try:
              y = float(x) / 2.54
              print("Résultat: " + x + " cm est égal à " + str(y) + " pouces")
              test = False
            except:
                print("Erreur: entrer un nombre.")
    print()
    if choix == "1":
        test = True
        while test == True:
            x = input("Enter votre nombre en pouces: ")
            try:
                y = float(x) * 2.54
                print("Résultat: " + x + " pouces est égal à " + str(y) + " cm")
                test = False
            except:
                print("Erreur: entrer un nombre.")
    print()