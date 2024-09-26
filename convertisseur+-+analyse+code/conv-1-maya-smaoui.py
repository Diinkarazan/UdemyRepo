condition = input("Choisissez le nombre correspondant à votre requête: 1) pouces vers cm    2) cm vers pouces. ")
 
if condition == "1":
    boucle = "2"
    while boucle == "2":
        valeur_pouces = input("Quelle est la valeur ( en pouces ) à convertir ? ")
        valeur1 = float(valeur_pouces)*2.54
        print("La valeur " + str(valeur_pouces) + " pouces vaut " + str(valeur1) + "cm.")
        boucle = input("Souhaitez vous sortir de la boucle ? 1. oui   2. non ? ")
 
if condition == "2":
    boucle = "2"
    while boucle == "2":
        valeur_cm = input("Quelle est la valeur ( en cm ) à convertir ? ")
        valeur2 = float(valeur_cm)*0.394
        print("La valeur " + str(valeur_cm) + "cm vaut " + str(valeur2) + " pouces.")
        boucle = input("Souhaitez vous sortir de la boucle ? 1. oui   2. non ? ")