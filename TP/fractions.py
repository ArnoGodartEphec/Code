""""
def pgcd(numerator, denominator):
    if numerator == 0:
        return denominator
    else:
        return pgcd(denominator % numerator, numerator)
"""

# PGCD class math
class Fraction:

    @property
    def numerator(self):
        return self.__num

    @property
    def denominator(self):
        return self.__den

    def __init__(self, num=0, den=1):
        """
        Implémentation d'une fraction avec un numérateur et un dénominateur
            PRE :   num : le numérateur de la fraction (un int)
                    den : le dénominateur de la fraction (un int)

            RAISE : den == 0, on ne peut pas diviser par 0
        """
        self.__num = num
        self.__den = den
        if den == 0:
            raise ZeroDivisionError("Le dénominateur ne peut pas être égal à zéro")
        if num == 0:
            self._numerator = 0
            self._denominator = 1
        else:
            if (num < 0 and den >= 0
                    or num >= 0 and den < 0):
                signe = -1
            else:
                signe = 1

    def __str__(self):
        """
        This builds a fraction based on some numerator and denominator.
        PRE : /
        POST : Renvoie une chaîne de caractères représentant la fraction avec le numérateur et le dénominateur
        """
        return str((self.numerator, self.denominator))

    def as_mixed_number(self):
        """
        Return a textual representation of the reduced form of the fraction.
        PRE : /
        POST : Renvoie une chaîne de caractères représentant la fraction sous la forme : nombre entier + fraction
        """

        if self.numerator > self.denominator:
            max_division = int(self.numerator // self.denominator)      # divison entiere
            reste_division = int(self.numerator % self.denominator)     # reste de la division , modulo
            if self.denominator == 1:                                   # Si le denom est egal à 1 = renvoyer la div ent
                return str(max_division)
            else:
                return str((max_division, reste_division, self.denominator))  # par ex 7/4 =
        return str((self.numerator, self.denominator))

    def __add__(self, other):
        """
        Overloading of the + operator for fractions
        PRE : other : fraction avec laquelle une autre fraction doit s'additionner
        POST : Renvoie le résultat de la somme des deux fractions
        """
        denominator = (self.denominator * other.denominator)
        numerator = (self.numerator * other.denominator) + (self.denominator * other.numerator)
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        """
        Overloading of the - operator for fractions
        PRE : other : fraction avec laquelle elle doit se soustraire
        POST : Renvoie une nouvelle fraction qui est le résultat de la somme avec la fraction qui est passée en paramètres
        """
        denominator = self.denominator * other.denominator
        numerator = (self.numerator * other.denominator) - (self.denominator * other.numerator)
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        """Overloading of the * operator for fractions
        PRE :  other : fraction avec laquelle elle doit se multiplier
        POST : Renvoie une nouvelle fraction qui est le résultat de la multiplication avec la fraction passée en paramètres
        """
        denominator = self.denominator * other.denominator
        numerator = self.numerator * other.numerator
        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions
        PRE :  other : fraction avec laquelle elle doit se diviser
        POST : Renvoie une nouvelle fraction qui est le résultat de la division avec la fraction passée en paramètres
        """
        if other.denominator == 0:
            raise ZeroDivisionError

        denominator = self.denominator * other.numerator
        numerator = self.numerator * other.denominator
        return Fraction(numerator, denominator)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions
        PRE : other : fraction avec laquelle elle doit s'élever à la puissance 2
        POST : Renvoie une nouvelle fraction qui est le résultat de la puissance avec la fraction passée en paramètres
        """
        denominator = self.denominator ** (other.numerator / other.denominator)
        numerator = self.numerator ** (other.numerator / other.denominator)
        return Fraction(numerator, denominator)

    # TODO : [BONUS] You can overload other operators if you wish


if __name__ == "__main__":
    Fraction()
