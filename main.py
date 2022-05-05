import math
suma = 0
lista = []

class Pracownik:
    def __init__(self, imie, pensja):
        self.imie = imie
        self.pensja = pensja
        self.emerytalna = round((self.pensja * 0.0976), 2)
        rentowa = round((self.pensja * 0.015), 2)
        chorobowa = round((self.pensja * 0.0245), 2)
        self.c = round((self.emerytalna + rentowa + chorobowa), 2)
        self.d = round((self.pensja - self.c), 2)
        self.e = round((self.d*0.09), 2)
        self.f = round((self.d*0.0775), 2)
        self.g = 111.25
        self.h = round(self.pensja - self.g - self.c)
        self.i = round((self.h * 0.18 - 46.33), 2)
        self.j = round(self.i - self.f)
        
        

    def netto(self):
        return round((self.pensja - self.c - self.e - self.j), 2)

    def koszt_prac(self):
        return round((self.pensja + self.skladki()), 2)

    def skladki(self):
        r2 = round((self.pensja * 0.065), 2)
        wyp = round((self.pensja * 0.0193), 2)
        fp = round((self.pensja * 0.0245), 2)
        fgsp = round((self.pensja * 0.001), 2)
        return round((self.emerytalna + r2 + wyp + fp + fgsp), 2)

n = input()
for i in range (0, int(n)):
    temp = input()
    temp = temp.split()
    lista.append(Pracownik(temp[0], int(temp[1])))

for i in range (len(lista)):
    p = lista[i]
    print(p.imie, "{:.2f}".format(p.netto()), "{:.2f}".format(p.skladki()), "{:.2f}".format(p.koszt_prac()))
    suma += p.koszt_prac()   
print(suma)