def pouce_cm(p):
    cm = p*2.54
    return cm
def cm_pouce(cm):
    p = cm/2.54
    return p
Astr = input("Taper 1 si vous souhaiter convertir de 'pouces vers cm' ou  Taper 2 pour 'cm vers pouces'")
a = int(Astr)
 
def print_pouce_cm():
    pouce = input('Entrer la valeur en pouce: ')
    cm = pouce_cm(int(pouce))
    print("Le résultat est "+str(cm)+"cm")
 
def print_cm_pouce():
    cm = input("Entrer la valeur en cm: ")
    pouce = cm_pouce(int(cm))   
    print("Le résultat est "+str(pouce)+"pouces")
 
if a==1:
    print_pouce_cm()
    test = input("Voulez-vous resaisir (y/n)?: ")
    while test == 'y':
        print_pouce_cm()
        test = input("Voulez-vous resaisir (y/n)?: ")
elif a == 2:
    print_cm_pouce()
    test = input("Voulez-vous resaisir (y/n)?: ")
    while test == 'y':
        print_pouce_cm()
        test = input("Voulez-vous resaisir (y/n)?: ")
else:
    print("Saisie Invalide !")