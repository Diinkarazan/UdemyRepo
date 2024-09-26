INCH = 2.54
CM = 0.394


def convert_inch2cm(value):
    return float(value)/float(INCH)


def convert_cm2inch(value):
    return float(value)*float(CM)


while True:
    choice = input("Que désirez-vous convertir: \n1) cm vers pouces\n2) pouces vers cm\nTapez 'X' pour sortir\n\nChoix : ")
    if choice == '1':
        input_value = input("Rentrez la valeur en cm à convertir en pouces : ")
        print(f"{input_value} cm correspond à {'%.3f' % convert_cm2inch(input_value)} pouces")
    elif choice == '2':
        input_value = input("Rentrez la valeur en pouces à convertir en cm : ")
        print(f"{input_value} pouces correspond à {'%.2f' % convert_cm2inch(input_value)} cm")
    elif choice == "x" or choice == "X":
        exit()
    else:
        print("Valeur incorrecte, merci de bien vouloir entrer un choix 1 ou 2\n")