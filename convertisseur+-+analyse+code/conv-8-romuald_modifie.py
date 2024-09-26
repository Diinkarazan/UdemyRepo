def demande_conversion():
    print("vous devez entrer a ou b")
    print("a = pouces vers cm")
    print("b = cm vers pouces")
    conversion =input(f" voulez vous convertire en a ou en b? ")
    return conversion

def demande_valeure(unite):
    valeure = input(f" quelle est la valeure à convertir en {unite}  ?")
    valeure_float = float(valeure)
    return valeure_float

conversion_entree = demande_conversion()
if conversion_entree == "a" :
    for valeure_entrer in range(0,2):
        valeure_entrer = demande_valeure("pouces vers cm")
        calcul = valeure_entrer * 2.5
        print(f"{calcul} cm")
elif conversion_entree == "b" :
    for valeure_entrer in range(0,2):
        valeure_entrer = demande_valeure("cm vers pouces")
        calcul = valeure_entrer * 0.394
        print(f"{calcul} pouces")