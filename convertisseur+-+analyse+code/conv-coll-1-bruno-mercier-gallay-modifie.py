def verif_reponse (choix):
    a = False
    while not a:
        try :
            choix = float(choix)
            return choix
        except :
            choix =input("ERREUR !  Rentrez une valeur numérique : ")
 
encore = True
while encore :
    choix = "0"
    while choix != "1" and choix != "2":
        choix = input("La conversion : de pouces vers cm (tapez 1) ou cm vers pouces (tapez 2) ")
 
    choix = int(choix)
    conversion = ((1, "pouces", "cm", 2.54),
                  (2, "cm", "pouces", 0.394))
    item_conversion = conversion[choix-1]
    unit1 = item_conversion[1]
    unit2 = item_conversion[2]
    facteur = item_conversion[3]
    val = input("Combien de " + unit1 + " ? ")
    verif_reponse(val)
    print()
    valeur_convertie = float(val)*facteur
    print(val, unit1, "=", valeur_convertie, unit2)
    print()
    choix = input("Encore ne conversion ? o/n ")
    print()
    if choix != "o" :
        break