def afficher_message():
    print("quel type de conversion souhaitez-vous faire?")
    print("1 : pouces vers cm")
    print("2 : cm vers pouces")
    print("3 : quitter")
 
def choisir_conversion():
    controle = 0
    afficher_message()#appel de la fonction affichage pour lister les options
    while controle == 0:
        choix = input("entrer le numéro correspondant à votre choix: ")
        if choix == "1":
            print("conversion pouces vers cm")
            controle = 1
        elif choix == "2":
            print("conversion cm vers pouces")
            controle = 2
        elif choix == "3":
            print("sortie...")
            controle = 3
        else:
            print("vous devez saisir 1 , 2 ou 3 selon la conversion souhaitée")
 
    return controle
 
def choix_valeur():
    valeur_int = 0
    controle = 0
    while controle == 0:
        valeur_str = input("saisissez la valeur à convertir : ")
        try:
            valeur_int = int(valeur_str)
            controle = 1
        except:
            print("ERREUR: vous devez saisir un nombre")
 
    return valeur_int
        
def conversion_cm_en_pouce(valeur):
    resultat = valeur * 0.394
    return resultat
def conversion_pouce_en_cm(valeur):
    resultat = valeur * 2.54
    return resultat
  
#------------PROGRAMME PRINCIPAL
print("Conversion d'unités")
controle = 0
while controle  == 0:
    type_conversion = choisir_conversion()
    if type_conversion == 3:# choix N°3 = sortie
        break
 
    valeur_initiale = choix_valeur()
 
    if type_conversion == 1:
        valeur_converti = conversion_pouce_en_cm(valeur_initiale)
        unite_initiale = "p"
        unite_convertie = "cm"
    else:
        valeur_converti = conversion_cm_en_pouce(valeur_initiale)
        unite_initiale = "cm"
        unite_convertie = "p"
#affichage du résultat
    print(f"conversion de {valeur_initiale} {unite_initiale} en {unite_convertie} est {valeur_converti} {unite_convertie}") 
 
    
print("fin du programme") 