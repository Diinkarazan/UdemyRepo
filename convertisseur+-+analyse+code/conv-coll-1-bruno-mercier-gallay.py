def verif_reponse (choix):
    a = False
    while not a:
        try :
            choix = float(choix)
            return
        except :
            choix =input("ERREUR !  Rentrez une valeur numérique : ")
 
encore = True
while encore :
    choix = "0"
    while choix != "1" and choix != "2":
        choix = input("La conversion : de pouces vers cm (tapez 1) ou cm vers pouces (tapez 2) ")
 
    choix = int(choix)
    conversion = ((1, "pouces", "cm", 2.54),(2, "cm", "pouces", 0.394))
    val = input("Combien de " + conversion[choix-1][1] + " ? ")
    verif_reponse(val)
    print()
    print(val, conversion[choix-1][1], "=", float(val)*conversion[choix-1][3], conversion[choix-1][2])
    print()
    choix = input("Encore ne conversion ? o/n ")
    print()
    if choix != "o" :
        break