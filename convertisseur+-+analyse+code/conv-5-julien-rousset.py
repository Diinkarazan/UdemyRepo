#Permet de demander la valeur à convertir et de procéder à une vérification bloquante pour éviter les erreurs classiques
def demanderValeur(type_valeur):
    valeur = input(f'Quel est la valeur à convertir en {type_valeur} ? ')
    try:
        valeur_int = int(valeur)
        return valeur_int
    except:
        try:
            valeur_int = float(valeur)
            return valeur_int
        except:
            print('Vous devez rentrer une valeur numérique !')
            return demanderValeur(type_valeur)
            
#Permet la conversion souhaitée
def Conversion(valeur, type_valeur):
    if type_valeur == 'cm':
        return valeur * 2.54
    else:
        return valeur * 0.394
 
#La fonction est capable de vérifier les commandes passés par l'utilisateur et peut boucler par récursion
def demanderUtilisateur():
    reponse_utils = input('Voulez-vous convertir en centimètres ou en pouce ? Répondez par "cm" ou "pouce" ou par "exit" pour fermer le programme: ')
    if reponse_utils == "exit":
        return
    elif reponse_utils != 'cm':
        if reponse_utils != "pouce":
            print('Vous devez rentrer soit "cm" ou "pouce"!')
            return demanderUtilisateur()
    
    valeur_convertir = demanderValeur(reponse_utils)
    print(f'{Conversion(valeur_convertir, reponse_utils)} {reponse_utils}')
    return demanderUtilisateur()
 
demanderUtilisateur()