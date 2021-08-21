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
# taille == 0 --> paramètres otpionnels

def afficher_informations(nom, age, taille = 0):
        print()
        # Plusieurs façons d'écrire le print mais donnant le même résultat
        print("Vous vous appelez : " + nom + ", vous avez" + str(age) + "ans")      # Classique en convertissant age en string, chaine concaténée
        print(f"Vous vous appelez {nom}, vous avez {age} ans")                      # Avec un f devant la chaine, chaine formatée
        print("Vous vous appelez %s et vous avez %s ans" %(nom, age))                # Avec le % , vieux format
        

    # == egal
    # <  inf
    # <= inf ou egal
    # > sup
    # >= sup ou egal
    # True / False

    # age  == 17 --> presque majeur
    # age  ==  --> majeur bravo
    # elif = elseif
    # age > 60 --> senior
    # age < 10 --> enfant
    # Attention à l'ordre des conditions    
    # Adolescent si age >= 12 et age < 18
    # Bebe si age == 1 ou age == 2
    
        if age == 17:
            print("presque majeur ")
        elif 12 <= age < 18 :
            print("Vous etes adolescent") 
        elif age == 1 or age == 2:
            print("Vous etes bebe") 
        elif age == 18:
            print("majeur tt pile bravo")
        elif age > 60:
            print("Vous etes senior")
        elif age < 10:
            print("Vous etes enfant")
        elif age >= 18:
            print("Vous etes majeur ")
        else:
            print("Vous etes mineur")

    # afficher la taille 
        if not taille == 0:
            print("Votre taille" + str(taille) + " m")
       



# Demander le nom de 2 personnes
#nom1 = demander_nom()
#nom2= demander_nom()

#nom1 = "Tat"
#nom2 = "tit"

# Demander l'age de 2 personnes

#age1 = demander_age(nom1)
#age2 = demander_age(nom2)

# Demander infos
#afficher_informations(nom1, age1)
#afficher_informations(nom2, age2)


# Boucle for
# Pour i de 0 à à 3
NB_PERSONNES = 1

for i in range(0, NB_PERSONNES):
    nom = "personne" + str(i+1)
    age = demander_age(nom)
    afficher_informations(nom, age)


print("""
    Print
        sur
            plusieurs
                niveaux

""")

print("toto", 20, "ans", "taille", 1.70)



    
