INCH_TO_CM = 2.54
CM_TO_INCH = 0.394
 
while True:
    value_choosen = input("Entrez la valeur et l'unité à convertir (cm ou pouce(s) / ou exit pour quitter):")
    if value_choosen == "exit":
        break
    splited_value = value_choosen.split()
    unite = splited_value[-1]
    valeur_a_convertir = splited_value[0]
 
    if not (unite == "cm" or unite == "pouce" or unite == "pouces"):
        print("Unité de mesure incorrecte.")
        continue

    try:
        valeur_a_convertir_float = float(valeur_a_convertir)
    except:
        print("Entrée invalide, veuillez réessayer.\n")
        continue

    if unite == "cm":
        print(f"{valeur_a_convertir_float} cm = {valeur_a_convertir_float*CM_TO_INCH} pouce(s)")
    else:
        print(f"{valeur_a_convertir_float} pouce(s) = {valeur_a_convertir_float*INCH_TO_CM} cm")