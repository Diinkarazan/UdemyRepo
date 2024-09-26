print("Choix de la conversion 1 ou 2 ")
print("1 : pouce vers centimètre")
print("2 : centimètre vers pouce")
 
choix = input("votre choix de la conversion est : ")
sortie_programme = "n"
while sortie_programme == "n":
    if choix == "1":
        valeur = float(input("votre valeur en inch est  : "))
        valeur_convertie = valeur * 2.54
        print(f"votre valeur en cm est : {valeur_convertie} cm")
        sortie_programme = input("vous voulez quittez y/n : ")
    else:
        valeur = float(input("votre valeur en cm est  : "))
        valeur_convertie = valeur * 0.394
        print(f"votre valeur en inch est  : {valeur_convertie} inch")
        sortie_programme = input("vous voulez quittez y/n : ")
 
print("fin de programme!!!!")