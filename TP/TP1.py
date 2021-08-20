from math import pi, sqrt

""" Périmètre cercle
r = rayon """

r = float(input("Introduisez un chiffre postif"))
print("Le périmètre du cercle de rayon",r, " est de ", pi*r**2)


"""Périmètre cercle
l et L 2 nbres positif """

longueur = float(input("Entrez un nombre positif"))
largeur = float(input("Entrez un nombre positif"))

try:
    P = (longueur + largeur)*2

except ValueError: 
    print("erreur")

else:
    print("Le périmètre est de ", P, "cm")



