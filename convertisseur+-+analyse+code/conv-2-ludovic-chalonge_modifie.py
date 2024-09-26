def choisir_conversion():
    print("quel type de conversion souhaitez-vous faire?")
    print("1 : pouces vers cm")
    print("2 : cm vers pouces")
    print("3 : quitter")

    while True:
        choix = input("entrer le numéro correspondant à votre choix: ")
        if choix == "1":
            print("conversion pouces vers cm")
            break
        elif choix == "2":
            print("conversion cm vers pouces")
            break
        elif choix == "3":
            print("sortie...")
            break
        print("ERREUR : Vous devez saisir 1 , 2 ou 3 selon la conversion souhaitée")
    return choix
 
def choix_valeur():
    while True:
        valeur_str = input("saisissez la valeur à convertir : ")
        try:
            valeur_float = float(valeur_str)
            break
        except:
            print("ERREUR: vous devez saisir un nombre")
    return valeur_float
        
def conversion_cm_en_pouce(valeur):
    resultat = valeur * 0.394
    return resultat
def conversion_pouce_en_cm(valeur):
    resultat = valeur * 2.54
    return resultat

def demander_valeur_et_afficher_conversion(fonction_de_version, unite_initiale, unite_convertie):
    valeur_initiale = choix_valeur()
    valeur_converti = fonction_de_version(valeur_initiale)
    print(f"conversion de {valeur_initiale} {unite_initiale} en {unite_convertie} est {valeur_converti} {unite_convertie}") 

#------------PROGRAMME PRINCIPAL
print("Conversion d'unités")
controle = 0
while controle  == 0:
    choix_conversion = choisir_conversion()

    if choix_conversion == "1":
        valeur_converti = demander_valeur_et_afficher_conversion(conversion_pouce_en_cm, "p", "cm")
    elif choix_conversion == "2":
        valeur_converti = demander_valeur_et_afficher_conversion(conversion_cm_en_pouce, "cm", "p")
    else: # choix N°3 = sortie
        break
 
#affichage du résultat
    
 
    
print("fin du programme") 