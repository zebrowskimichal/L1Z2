
##1
class Punkt():
    ##9
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        print("Utworzono punkt: (" + str(self.x) + ", " + str(self.y) + ")")
##3
    def wyswietl(self):
        print("Wspolrzedne punktu to (" + str(self.x) + ", " + str(self.y) + ")")
##4
    def pobierzX(self):
        return x

    def pobierzX(self):
        return y
##6
    def ustawXY(self, ustawx, ustawy):
        self.x = int(ustawx)
        self.y = int(ustawy)
##7
    def ustawXYpunkt(self, punkt):
        self.x = punkt.x
        self.y = punkt.y
##8
    def pobierzWsp(self):
        return Punkt(self.x, self.y)
##2
pierwszy = Punkt(1, 2)
drugi = Punkt(5, 3)
print("Wspolrzedne punktu to (" + str(pierwszy.x) + ", " + str(pierwszy.y) + ")")
print("Wspolrzedne punktu to (" + str(drugi.x) + ", " + str(drugi.y) + ")")

##9
obiekt1 = Punkt(1, 8)
obiekt2 = Punkt(6, 8)

"""
Wywołanie konstruktora printuje napis: Utworzono punkt: ($x, $y)
"""

##10
obiekt3 = Punkt()
"""
Wyskakuje błąd: Exception has occurred: TypeError
Punkt.__init__() missing 2 required positional arguments: 'x' and 'y'
"""