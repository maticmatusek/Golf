import random
import math

#Ugotovi kaj in kako boš, če sta na istem mestu igralca
#ugotovi kaj se zgodi, če gre igralec izven polja
#slovar je oblike {0: ['ime', (x, y)]}
#mislim, da bi moralo do sedaj vse delovati, kot se spodobi


class Igra:

    def __init__(self, pozicija_luknje, igralec_na_vrsti, koordinate_zacetka):
        self.igralci = {}
        self.runda = 0
        self.pozicija_luknje = pozicija_luknje
        self.igralec_na_vrsti = igralec_na_vrsti
        self.koordinate_zacetka = koordinate_zacetka
        self.koncani_igralci = {}


    def __str__(self):
        return f"Pozicija luknje je {self.pozicija_luknje}, igralec, ki je na vrsti je igralec številka {self.igralec_na_vrsti}, začetne koordinate so {self.koordinate_zacetka}, igralci so {self.igralci}"

    def dodaj_igralca(self, ime_igralca):
        stevilka_igralca = len(self.igralci)
        koordinata_x, koordinata_y = self.koordinate_zacetka
        self.igralci[stevilka_igralca] = [ime_igralca, (koordinata_x, koordinata_y)]
        #doda igralca med množico igralcev in jih oštevilči od skupaj z 0 naprej

    def udarec(self, moc, kot):
        if self.igralec_na_vrsti == min(self.igralci.keys()):
            self.runda = self.runda + 1
        #vsakič ko je krog okoli prišteje eno rundo
        premik_x, premik_y = izracun_premika(moc, kot)
        trenuten_x, trenuten_y = self.igralci[self.igralec_na_vrsti][1]
        novi_x = trenuten_x + premik_x
        novi_y = trenuten_y - premik_y
        self.igralci[self.igralec_na_vrsti][1] = (novi_x, novi_y)
        #izračuna nove koordinate glede na funkcijo izracunaj_premik
        if self.igralec_na_vrsti < max(self.igralci.keys()):
            self.igralec_na_vrsti = self.igralec_na_vrsti + 1
            while self.igralec_na_vrsti not in self.igralci.keys():
                self.igralec_na_vrsti = self.igralec_na_vrsti + 1
        elif self.igralec_na_vrsti == max(self.igralci.keys()):
            self.igralec_na_vrsti = min(self.igralci.keys())
        #spremeni igralca,ki je na vrsti
        self.igralec_koncal()    
        #preveri, če je igralec končal
        ########POPRAVI,DA NI TOK VELIK V ENI FUNKCIJI !!!!!!!!!!!!!



        
    def igralec_koncal(self):
        for i in self.igralci.keys():
            if self.igralci[i][1] == self.pozicija_luknje :
                ime_igralca = self.igralci[i][0]
                self.koncani_igralci[ime_igralca] = self.runda
                self.igralci.pop(i)
                break
            else:
                pass
        #preveri, če je igralec končal in ga vrže ven iz igre,
        #ter ga doda na seznam igralcev, ki so končali skupaj s številom rund





def nova_igra():
    x_koordinata_luknje = random.randint(6, 10)
    y_koordinata_luknje = random.randint(1, 4)
    x_koordinata_zacetka = random.randint(1, 4)
    y_koordinata_zacetka = random.randint(6, 10)
    return Igra((x_koordinata_luknje, y_koordinata_luknje), 0, (x_koordinata_zacetka, y_koordinata_zacetka))
    #naredi novo igro brez igralcev, igralce je treba dodati z metodo .dodaj_igralca,
    #vsem se na začetku priredi enaka pozicija


def izracun_premika(moc, kot):
    premik_koordinate_x = round(math.cos(math.radians(kot)) * moc)
    premik_koordinate_y = round(math.sin(math.radians(kot)) * moc)
    return (premik_koordinate_x, premik_koordinate_y)
    #izračuna premik glede na kot in moč,
    #pozor y os je pozitivna navzdol, zato se v metodi, udarec y odšteje


I = nova_igra()
I.dodaj_igralca("Matic")
#I.dodaj_igralca("Iza")
#I.dodaj_igralca("Maja")
#I.dodaj_igralca("Martin")
#I.dodaj_igralca("Seba")
#I.dodaj_igralca("Nina")
print(I)
#I.udarec(1,0)
#udarec(10,45)
#udarec(10,90)
#udarec(10,135)
#udarec(10,180)
#udarec(10,225)
#udarec(10,270)
#udarec(10,315)
