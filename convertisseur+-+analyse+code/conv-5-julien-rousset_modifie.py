#Permet de demander la valeur à convertir et de procéder à une vérification bloquante pour éviter les erreurs classiques
def demanderValeur(type_valeur):
    valeur = input(f'Quel est la valeur à convertir en {type_valeur} ? ')
    try:
        valeur_float = float(valeur)
        return valeur_float
    except:
        print('Vous devez rentrer une valeur numérique !')
    return demanderValeur(type_valeur)
            
#Permet la conversion souhaitée
def Conversion(valeur, type_valeur):
    if type_valeur == 'cm':
        return valeur * 2.54
    return valeur * 0.394
 
#La fonction est capable de vérifier les commandes passés par l'utilisateur et peut boucler par récursion
def demanderUtilisateur():
    unite_choisie = input('Voulez-vous convertir en centimètres ou en pouce ? Répondez par "cm" ou "pouce" ou par "exit" pour fermer le programme: ')
    if unite_choisie == "exit":
        return
    elif unite_choisie != 'cm' and unite_choisie != "pouce":
        print('Vous devez rentrer soit "cm" ou "pouce"!')
        return demanderUtilisateur()
    
    valeur_a_convertir = demanderValeur(unite_choisie)
    valeur_convertie = Conversion(valeur_a_convertir, unite_choisie)
    print(f'{valeur_convertie} {unite_choisie}')
    return demanderUtilisateur()
 
demanderUtilisateur()