from math import pi, sqrt

""" Périmètre cercle
r = rayon 

r = float(input("Introduisez un chiffre postif"))
print("Le périmètre du cercle de rayon",r, " est de ", pi*r**2)


Périmètre cercle
l et L 2 nbres positif 

longueur = float(input("Entrez un nombre positif"))
largeur = float(input("Entrez un nombre positif"))

try:
    P = (longueur + largeur)*2

except ValueError: 
    print("erreur")

else:
    print("Le périmètre est de ", P, "cm") 
    
"""

"""
n=0 
while n < 10:
    print("Valeur de n: ", n)
    n = n+1
"""

"""
mot_de_passe = ""
while not mot_de_passe == "TOTO":
    mot_de_passe = input(" Quel est le mdp ? ")
print("Bien joué")
"""
"""
age = 0
while age == 0:
    age_str = input(" Quel est votre age ? ")
    try:
        age = int(age_str)
    except:
        print("ERREUR")

print(" Vous avez " + str(age) + " ans " )
print(" L'an prochain vous aurez " +  str(age + 1) + " ans ")

nom = ""
while nom == "":
    rep = input(" Quel est votre nom ? ")
"""

# Version avec fonctions

def demander_nom():
    nom =""
    while nom == "":
        nom = input(" Quel est votre nom ? ")
    return nom



def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " Quel est votre age ? ")
        try:
            age_int = int(age_str)
        except:
            print("ERREUR")
    return age_int

# afficher les infos
def afficher_informations(nom, age):
        print("Vous etes: ", nom)
        print(" Vous avez : ", age)


# Demander le nom de 2 personnes
nom1 = demander_nom()
nom2= demander_nom()

# Demander l'age de 2 personnes
age1 = demander_age(nom1)
age2 = demander_age(nom2)

# Demander infos
afficher_informations(nom1, age1)
afficher_informations(nom2, age2)










    
