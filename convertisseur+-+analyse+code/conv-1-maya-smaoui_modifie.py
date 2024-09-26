choix_conversion = input("Choisissez le nombre correspondant à votre requête:\n1) pouces vers cm\n2) cm vers pouces.\nVotre choix (1 ou 2) : ")
 
if choix_conversion == "1":
    boucle = "2" # 2 correspond au choix utilisateur pour reboucler
    while boucle == "2":
        valeur_pouces = input("Quelle est la valeur ( en pouces ) à convertir ? ")
        valeur_convertie = float(valeur_pouces)*2.54
        print("La valeur " + str(valeur_pouces) + " pouces vaut " + str(valeur_convertie) + "cm.")
        boucle = input("Souhaitez vous sortir de la boucle ? 1. oui   2. non (choisissez 1 ou 2) : ")
 
if choix_conversion == "2":
    boucle = "2"
    while boucle == "2":
        valeur_cm = input("Quelle est la valeur ( en cm ) à convertir ? ")
        valeur_convertie = float(valeur_cm)*0.394
        print("La valeur " + str(valeur_cm) + "cm vaut " + str(valeur_convertie) + " pouces.")
        boucle = input("Souhaitez vous sortir de la boucle ? 1. oui   2. non ? ")