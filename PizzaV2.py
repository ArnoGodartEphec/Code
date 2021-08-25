# Script affichant des pizzas
# nom, prix, ingrédients, végétarienne ou non

class Pizza:

    def __init__(self, nom, prix, ingredients, vegetarienne=False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarienne=vegetarienne


    def Afficher(self):
        veg_str = ""
        if self.vegetarienne:
            veg_str = "- Végétarienne"
        print(f"Pizza {self.nom} : {self.prix}€" + veg_str)
        print(", ".join(self.ingredients))
        print()


class PizzaPerso(Pizza):
    PRIX_DE_BASE = 7
    PRIX_PAR_INGREDIENT = 1
    dernier_numero = 0

    def __init__(self):
        PizzaPerso.dernier_numero += 1
        self.numero = PizzaPerso.dernier_numero
        super().__init__("Personnalisée " + str(self.numero), 0, [])
        self.demander_ingredients()
        self.calculer_prix()

    def demander_ingredients(self):
        print()
        print(f"Ingrédients pour la pizza personnalisée {self.numero}")
        while True:
            ingredient = input("Ajoutez un ingrédient (ou ENTER pour terminer)")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f"Vous avez {len(self.ingredients)} ingrédient(s) : {', '.join(self.ingredients)}")

    def calculer_prix(self):
        self.prix = self.PRIX_DE_BASE + len(self.ingredients)*self.PRIX_PAR_INGREDIENT


# liste des Pizzas
pizzas = [
    Pizza("Speciale", 8.5, ("emmental", "brie"), True),
    Pizza("Hawai", 9.6, ("tomate", "ananas")),
    Pizza("Bbq", 14, ("emmental", "brie")),
    Pizza("Yes", 75, ("radis", "loukoum"), True),
    PizzaPerso(),
    PizzaPerso()
    ]

def tri(e):
    return e.prix


# pizzas.sort(key=tri)

# boucle pour afficher
for i in pizzas:
    if  i.prix < 10:
        i.Afficher()


