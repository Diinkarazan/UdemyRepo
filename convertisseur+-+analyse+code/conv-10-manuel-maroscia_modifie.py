titre="Convertisseur de pouces en centimètres et viceversa"
l=len(titre)+4
print('*'*l)
print("* "+titre+" *")
print("*"*l)
print("Choisissez un type de conversion:")
print("------------------------------")
print("a) pouces vers cm")
print("b) cm vers pouces")
print()
 
while True:
    reponse=input("Faites votre choix a ou b : ")
    if reponse=='a' or reponse=='b':
        break
    print("ERREUR: Vous devez choisir a ou b")
 
if reponse=='a':
 while True:
  p=input('Entrez une valeur en pouce: ')
  try:
   n=round(float(p)*2.54,2)
  except:
    print("Merci de saisir une valeur numérique !")
    continue
  print(f"{p} pouce = {n:0.2f} cm")
  r=input("Tapez q pour arrêter la conversion ou ENTER pour continuer: ")
  if r=="q":
    break
        
elif reponse=='b':
 while True:
  p=input('Entrez une valeur en cm: ')
  try:
    n=round(float(p)/2.54,2)
  except:
    print("Merci de saisir une valeur numérique !")
    continue
  print(p+" cm = "+str(n)+" pouces")
  r=input("Tapez q pour arrêter la conversion: ")
  if r=="q":
    break