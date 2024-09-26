def demande_conversion():
    print("vous devez entrer a ou b")
    a = "pouces vers cm"
    b = "cm vers pouces"
    print("a = pouces vers cm")
    print("b = cm vers pouces")
    conversion =input(f" voulez vous convertire en a ou en b? ")
    return conversion
def demande_valeure1(a1):
    valeure = input(f" quelle est la valeure à  convertire en {a1}  ?")
    valeure_int = int(valeure)
    return valeure_int
def demande_valeure2(b1):
    valeure = input(f" quelle est la valeure à convertire en {b1} ?")
    valeure_int = int(valeure)
    return valeure_int

a = "pouces vers cm"
b = "cm vers pouces"
conversion_entrer = demande_conversion()
if conversion_entrer == "a" :
    for valeure_entrer in range(0,2):
        valeure_entrer = demande_valeure1(a)
        calcul = valeure_entrer * 2.5
        print(f"{calcul} cm")
elif conversion_entrer == "b" :
    for valeure_entrer in range(0,2):
        valeure_entrer = demande_valeure2(b)
        calcul = valeure_entrer * 0.394
        print(f"{calcul} pouces")