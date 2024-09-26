# Fonctions qui assure la conversion des valeurs
def pouces_vers_centimetres(a):
    return round(a * 2.54, 2)
 
def centimetres_vers_pouces(a):
    return round(a * 0.394, 2)
 
 
# La fonction demande à l'utilisateur de choisir le mode de conversion et gère le exit
def demander_mode_conversion_utilisateur(l_mode):
    print("Quel type de conversion, souhaitez-vous utiliser ?")
    for i in range(len(l_mode)):
        print(f"{i+1} - {l_mode[i][0]}")
    
    while True:
        try:
            choix = int(input(f"Votre choix (entre 1 et {len(l_mode)}): "))
            if 1 <= choix <= len(l_mode):
                break
        
            print(f"Erreur: Vous devez rentrer un nombre compris entre 1 et {len(l_mode)}")
        
        except ValueError:
            print("Erreur: Vous devez rentrer un nombre")
 
    if choix == 3:
        print("À bientôt !")
        exit()
 
    unite_avant_conversion = l_mode[int(choix) - 1][1]
 
    return choix, unite_avant_conversion
 
 
# La fonction demande à l'utilisateur une valeur et la calcule selon le mode choisi
def demander_valeur_utilisateur_et_calculer(mode_choisi, unite_avant_conversion):
    l_valeurs = []
    l_unites = []
    l_resultats = []
    while True:
        try:
            valeur = int(input(f"Entrez la valeur à convertir (en {unite_avant_conversion}): "))
            if mode_choisi == 1:
                resultat = pouces_vers_centimetres(valeur)
                unite_apres_conversion = liste_modes_conversion[mode_choisi-1][2]
                
 
            elif mode_choisi == 2:
                resultat = centimetres_vers_pouces(valeur)
                unite_apres_conversion = liste_modes_conversion[mode_choisi-1][2]
 
            l_valeurs.append(valeur)
            l_resultats.append(resultat)
            l_unites.append(unite_apres_conversion)
                
 
        except ValueError:
                print("Erreur: Vous devez rentrer un nombre")
                return demander_valeur_utilisateur_et_calculer(mode_choisi, unite_avant_conversion)
        
        print()
 
        if not ajout_valeur_supplementaire():
            break
 
    print()
 
 
    return (l_valeurs, unite_avant_conversion, l_resultats, l_unites)
            
 
# La fonction demande à l'utilisateur, si il veut ajouter une valeur du même type à convertir
def ajout_valeur_supplementaire():
    while True:
        print()
        print("Souhaitez-vous ajouter une autre valeur du même type à convertir ?")
        print("1 - Oui")
        print("2 - Non")
        choix = input("Votre choix (entre 1 et 2): ")
 
        if choix == "1":
            return True
        elif choix == "2":
            return False
 
        print("Erreur: Choissisez entre les 2 choix disponibles")
 
 
 
# Cette fonction se charge d'afficher le(s) résultat(s)
def afficher_valeur_convertie(valeurs_uniteAv_resultats_et_uniteAp):
    print("Le(s) résultat(s) :")
    for i in range(len(valeurs_uniteAv_resultats_et_uniteAp[0])):
        print(f"{valeurs_uniteAv_resultats_et_uniteAp[0][i]} {valeurs_uniteAv_resultats_et_uniteAp[1]} correspond à {valeurs_uniteAv_resultats_et_uniteAp[2][i]} {valeurs_uniteAv_resultats_et_uniteAp[3][i]}")
 
 
 
# Une liste qui contient des tuples, chaque tuples contient le mode de conversion et les unités (avant et après conversion)
liste_modes_conversion = [("Pouces vers Centimètres", "pouces", "cm"), 
                          ("Centimètres vers Pouces", "cm", "pouces"),
                          ("Exit", ""),]
 
 
# Programme Principal 
print("Bienvenue ! ")
while True:
    
    mode_choisi, unite = demander_mode_conversion_utilisateur(liste_modes_conversion)
 
    valeurs_uniteAv_resultats_et_uniteAp = demander_valeur_utilisateur_et_calculer(mode_choisi, unite)
 
    afficher_valeur_convertie(valeurs_uniteAv_resultats_et_uniteAp)
    
    print()