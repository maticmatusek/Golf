import random
import math
import json


DATOTEKA_S_STANJEM = "stanje.json"


class Igra:

    def __init__(self, pozicija_luknje, igralec_na_vrsti, koordinate_zacetka, igralci=None, koncani_igralci=None, runda=None, ):
        if igralci is None:
            self.igralci = {}
        else:
            self.igralci = igralci
        if runda is None:
            self.runda = 0
        else:
            self.runda = runda
        if koncani_igralci is None:
            self.koncani_igralci = []
        else:
            self.koncani_igralci = koncani_igralci
        self.pozicija_luknje = pozicija_luknje
        self.igralec_na_vrsti = igralec_na_vrsti
        self.koordinate_zacetka = koordinate_zacetka

    def dodaj_igralca(self, ime_igralca):
        stevilo_udarcev = 0
        stevilka_igralca = len(self.igralci)
        koordinata_x, koordinata_y = self.koordinate_zacetka
        self.igralci[stevilka_igralca] = [ime_igralca,
                                          (koordinata_x, koordinata_y), stevilo_udarcev]
        # doda igralca med množico igralcev in jih oštevilči od skupaj z 0 naprej

    def udarec(self, moc, kot):
        if moc > 100 or moc < 0:
            return "Moč je vrednost med 0 in 100"
        self.nova_runda()
        premik_x, premik_y = izracun_premika(moc, kot)
        trenuten_x, trenuten_y = self.igralci[self.igralec_na_vrsti][1]
        novi_x = trenuten_x + premik_x
        novi_y = trenuten_y - premik_y
        self.igralci[self.igralec_na_vrsti][2] = self.igralci[self.igralec_na_vrsti][2] + 1
        nove_koordinate = self.preveri_isto_mesto(novi_x, novi_y)
        posodobljen_x, posodobljen_y = nove_koordinate
        if preveri_udarec(posodobljen_x, posodobljen_y):
            self.igralci[self.igralec_na_vrsti][1] = (
                posodobljen_x, posodobljen_y)

            self.naslednji_igralec()
            self.igralec_koncal()
            return "Vredu"
        else:
            self.naslednji_igralec()
            self.igralec_koncal()
            return "Napaka"

    def naslednji_igralec(self):
        if self.igralec_na_vrsti < max(self.igralci.keys()):
            self.igralec_na_vrsti = self.igralec_na_vrsti + 1
            while self.igralec_na_vrsti not in self.igralci.keys():
                self.igralec_na_vrsti = self.igralec_na_vrsti + 1
        elif self.igralec_na_vrsti == max(self.igralci.keys()):
            self.igralec_na_vrsti = min(self.igralci.keys())

    def nova_runda(self):
        mnozica = set()
        for i in self.igralci:
            mnozica.add(self.igralci[i][2])
        self.runda = min(mnozica) + 1
        # ko imajo vsi igralci isto število udarcev, se runda zamenja

    def igralec_koncal(self):
        for i in self.igralci.keys():
            if self.igralci[i][1] == self.pozicija_luknje:
                ime_igralca = self.igralci[i][0]
                koncani_igralec = ime_igralca, self.runda
                self.koncani_igralci.append(koncani_igralec)
                self.igralci.pop(i)
                break
            else:
                pass
        # preveri, če je igralec končal in ga vrže ven iz igre,
        # ter ga doda na seznam igralcev, ki so končali skupaj s številom rund

    def preveri_isto_mesto(self, novi_x, novi_y):
        mnozica = set()
        nove_koordinate = novi_x, novi_y
        nove_koordinate1 = novi_x, novi_y + 1
        nove_koordinate2 = novi_x, novi_y - 1
        nove_koordinate3 = novi_x + 1, novi_y
        nove_koordinate4 = novi_x - 1, novi_y
        nove_koordinate5 = novi_x + 1, novi_y + 1
        nove_koordinate6 = novi_x - 1, novi_y + 1
        nove_koordinate7 = novi_x + 1, novi_y - 1
        nove_koordinate8 = novi_x - 1, novi_y - 1
        for i in self.igralci.keys():
            mnozica.add(self.igralci[i][1])
        if nove_koordinate not in mnozica:
            return nove_koordinate
        elif nove_koordinate1 not in mnozica:
            return nove_koordinate1
        elif nove_koordinate2 not in mnozica:
            return nove_koordinate2
        elif nove_koordinate3 not in mnozica:
            return nove_koordinate3
        elif nove_koordinate4 not in mnozica:
            return nove_koordinate4
        elif nove_koordinate5 not in mnozica:
            return nove_koordinate5
        elif nove_koordinate6 not in mnozica:
            return nove_koordinate6
        elif nove_koordinate7 not in mnozica:
            return nove_koordinate7
        elif nove_koordinate8 not in mnozica:
            return nove_koordinate8


def preveri_udarec(novi_x, novi_y):
    if novi_x > 100 or novi_y > 100 or novi_x < 0 or novi_y < 0:
        return False
    else:
        return True


def nova_igra1(igra=random.randint(1, 5)):
    if igra == 1:
        x_koordinata_luknje = random.randint(60, 100)
        y_koordinata_luknje = random.randint(1, 40)
        x_koordinata_zacetka = random.randint(1, 40)
        y_koordinata_zacetka = random.randint(60, 100)
        return Igra((x_koordinata_luknje, y_koordinata_luknje), 0, (x_koordinata_zacetka, y_koordinata_zacetka))
    if igra == 2:
        x_koordinata_zacetka = random.randint(60, 100)
        y_koordinata_zacetka = random.randint(1, 40)
        x_koordinata_luknje = random.randint(1, 40)
        y_koordinata_luknje = random.randint(60, 100)
        return Igra((x_koordinata_luknje, y_koordinata_luknje), 0, (x_koordinata_zacetka, y_koordinata_zacetka))
    if igra == 3:
        x_koordinata_luknje = random.randint(1, 40)
        y_koordinata_luknje = random.randint(1, 40)
        x_koordinata_zacetka = random.randint(60, 100)
        y_koordinata_zacetka = random.randint(60, 100)
        return Igra((x_koordinata_luknje, y_koordinata_luknje), 0, (x_koordinata_zacetka, y_koordinata_zacetka))
    if igra == 4:
        x_koordinata_luknje = random.randint(60, 100)
        y_koordinata_luknje = random.randint(60, 100)
        x_koordinata_zacetka = random.randint(1, 40)
        y_koordinata_zacetka = random.randint(1, 40)
        return Igra((x_koordinata_luknje, y_koordinata_luknje), 0, (x_koordinata_zacetka, y_koordinata_zacetka))
    if igra == 5:
        pod_igra = random.randint(1, 4)
        x_koordinata_luknje = random.randint(35, 65)
        y_koordinata_luknje = random.randint(35, 65)
        if pod_igra == 1:
            x_koordinata_zacetka = random.randint(1, 100)
            y_koordinata_zacetka = random.randint(1, 20)
            return Igra((x_koordinata_luknje, y_koordinata_luknje), 0, (x_koordinata_zacetka, y_koordinata_zacetka))
        if pod_igra == 2:
            x_koordinata_zacetka = random.randint(1, 100)
            y_koordinata_zacetka = random.randint(80, 100)
            return Igra((x_koordinata_luknje, y_koordinata_luknje), 0, (x_koordinata_zacetka, y_koordinata_zacetka))
        if pod_igra == 3:
            x_koordinata_zacetka = random.randint(1, 20)
            y_koordinata_zacetka = random.randint(1, 100)
            return Igra((x_koordinata_luknje, y_koordinata_luknje), 0, (x_koordinata_zacetka, y_koordinata_zacetka))
        if pod_igra == 4:
            x_koordinata_zacetka = random.randint(80, 100)
            y_koordinata_zacetka = random.randint(1, 100)
            return Igra((x_koordinata_luknje, y_koordinata_luknje), 0, (x_koordinata_zacetka, y_koordinata_zacetka))
    # naredi novo igro brez igralcev, igralce je treba dodati z metodo .dodaj_igralca,
    # vsem se na začetku priredi enaka pozicija


def izracun_premika(moc, kot):
    premik_koordinate_x = round(math.cos(math.radians(kot)) * moc)
    premik_koordinate_y = round(math.sin(math.radians(kot)) * moc)
    return (premik_koordinate_x, premik_koordinate_y)
    # izračuna premik glede na kot in moč,
    # pozor y os je pozitivna navzdol, zato se v metodi, udarec y odšteje


class Golf:

    def __init__(self, datoteka_s_stanjem):
        self.igre = {}
        self.datoteka_s_stanjem = datoteka_s_stanjem

    def prost_id_igre(self):
        mnozica = []
        for i in self.igre.keys():
            mnozica.append(int(i))
        if len(self.igre) == 0:
            return 0
        else:
            return max(mnozica) + 1

    def udarec(self, id_igre, moc, kot):
        self.nalozi_igre_iz_datoteke()
        igra = self.igre[id_igre]
        preveri = igra.udarec(moc, kot)
        if preveri == "Vredu":
            self.igre[id_igre] = igra
            self.zapisi_igre_v_datoteko()
            return "Vredu"
        else:
            self.igre[id_igre] = igra
            self.zapisi_igre_v_datoteko()
            return "Napaka"

    def dodaj_igralca(self, id_igre, ime):
        self.nalozi_igre_iz_datoteke()
        igra = self.igre[id_igre]
        igra.dodaj_igralca(ime)
        self.igre[id_igre] = igra
        self.zapisi_igre_v_datoteko()

    def nova_igra(self, stevilka_igre=random.randint(1, 5)):
        self.nalozi_igre_iz_datoteke()
        id_igre = self.prost_id_igre()
        igra = nova_igra1(stevilka_igre)
        self.igre[id_igre] = igra
        self.zapisi_igre_v_datoteko()
        return id_igre

    # def zapisi_igre_v_datoteko(self):
     #   with open(self.datoteka_s_stanjem, "w", encoding="utf-8") as f:
      #      igre = {id_igre: (igra.igralci, igra.runda, igra.pozicija_luknje, igra.igralec_na_vrsti,
       #                       igra.koordinate_zacetka, igra.koncani_igralci) for id_igre, igra in self.igre.items()}
        #    json.dump(igre, f)

    def zapisi_igre_v_datoteko(self):
        igre = {}
        with open(self.datoteka_s_stanjem, "w", encoding="utf-8") as f:
            for id_igre, igra in self.igre.items():
                igre[id_igre] = (igra.igralci, igra.runda, igra.pozicija_luknje,
                                 igra.igralec_na_vrsti, igra.koordinate_zacetka, igra.koncani_igralci)
            json.dump(igre, f)

    # def nalozi_igre_iz_datoteke(self):
     #   with open(self.datoteka_s_stanjem, "r", encoding="utf-8") as f:
      #      igre = json.load(f)
       #     self.igre = {int(id_igre): (Igra(pozicija_luknje, igralec_na_vrsti, koordinate_zacetka, igralci, koncani_igralci, runda)
        #                                for id_igre, (igralci, runda, pozicija_luknje, igralec_na_vrsti, koordinate_zacetka, koncani_igralci) in igre.items())}

    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem, "r", encoding="utf-8") as f:
            igre = json.load(f)
            for id_igre, (igralci, runda, pozicija_luknje, igralec_na_vrsti, koordinate_zacetka, koncani_igralci) in igre.items():
                self.igre[id_igre] = Igra(
                    pozicija_luknje, igralec_na_vrsti, koordinate_zacetka, igralci, koncani_igralci, runda)
