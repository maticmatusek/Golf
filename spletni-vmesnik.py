import bottle
import model
SKRIVNOST = "skrivnost je skrivnost"



@bottle.get("/")
def osnovna_stran():
    return bottle.template("osnovna.html")


@bottle.get("/igra")
def igra_stran():
    golf = model.Golf.nalozi_iz_jsona(model.DATOTEKA_S_STANJEM)
    id_igre = int(bottle.request.get_cookie("idigre" , secret=SKRIVNOST).split("e")[1])
    igra = golf.igre[id_igre]
    igralci = igra.igralci
    x_koordinata_luknje, y_koordinata_luknje = igra.pozicija_luknje
    pozicija_luknje = igra.pozicija_luknje
    igralec_na_vrsti = igra.igralec_na_vrsti
    koordinate_zacetka = igra.koordinate_zacetka
    runda = igra.runda
    koncani_igralci = igra.koncani_igralci
    return bottle.template("igra.html",igralci=igralci ,x_koordinata_luknje=x_koordinata_luknje,y_koordinata_luknje=y_koordinata_luknje,pozicija_luknje=pozicija_luknje,igralec_na_vrsti=igralec_na_vrsti,koordinate_zacetka=koordinate_zacetka,runda=runda,koncani_igralci=koncani_igralci)


@bottle.get("/nova-igra/")
def preusmeritev_na_izbiro_igre():
    bottle.redirect("/izbira-igre/")


@bottle.get("/izbira-igre/")
def izibra_igre():
    return bottle.template("izbira.html")


@bottle.post("/izbrana-igra/1")
def ena():
    golf = model.Golf.nalozi_iz_jsona(model.DATOTEKA_S_STANJEM)
    id_igre = golf.nova_igra(1)
    bottle.response.set_cookie("idigre", "idigre{}".format(
        id_igre), path="/", secret=SKRIVNOST)
    bottle.redirect("/dodajanje-igralcev/")


@bottle.post("/izbrana-igra/2")
def dva():
    golf = model.Golf.nalozi_iz_jsona(model.DATOTEKA_S_STANJEM)
    id_igre = golf.nova_igra(2)
    bottle.response.set_cookie("idigre", "idigre{}".format(
        id_igre), path="/", secret=SKRIVNOST)
    bottle.redirect("/dodajanje-igralcev/")


@bottle.post("/izbrana-igra/3")
def tri():
    golf = model.Golf.nalozi_iz_jsona(model.DATOTEKA_S_STANJEM)
    id_igre = golf.nova_igra(3)
    bottle.response.set_cookie("idigre", "idigre{}".format(
        id_igre), path="/", secret=SKRIVNOST)
    bottle.redirect("/dodajanje-igralcev/")


@bottle.post("/izbrana-igra/4")
def stiri():
    golf = model.Golf.nalozi_iz_jsona(model.DATOTEKA_S_STANJEM)
    id_igre = golf.nova_igra(4)
    bottle.response.set_cookie("idigre", "idigre{}".format(
        id_igre), path="/", secret=SKRIVNOST)
    bottle.redirect("/dodajanje-igralcev/")


@bottle.post("/izbrana-igra/5")
def pet():
    golf = model.Golf.nalozi_iz_jsona(model.DATOTEKA_S_STANJEM)
    id_igre = golf.nova_igra(5)
    bottle.response.set_cookie("idigre", "idigre{}".format(
        id_igre), path="/", secret=SKRIVNOST)
    bottle.redirect("/dodajanje-igralcev/")


@bottle.post("/izbrana-igra/6")
def random():
    golf = model.Golf.nalozi_iz_jsona(model.DATOTEKA_S_STANJEM)
    id_igre = golf.nova_igra()
    bottle.response.set_cookie("idigre", "idigre{}".format(
        id_igre), path="/", secret=SKRIVNOST)
    bottle.redirect("/dodajanje-igralcev/")


@bottle.get("/dodajanje-igralcev/")
def stran_dodajanja():
    golf = model.Golf.nalozi_iz_jsona(model.DATOTEKA_S_STANJEM)
    id_igre = int(bottle.request.get_cookie("idigre" , secret=SKRIVNOST).split("e")[1])
    igra = golf.igre[id_igre]
    igralci = igra.igralci
    napaka = {}
    return bottle.template("dodajanje-igralcev.html", igra = igra, igralci = igralci , napaka = napaka)


@bottle.post("/dodaj-igralca/")
def dodaj_igralca():
    golf = model.Golf.nalozi_iz_jsona(model.DATOTEKA_S_STANJEM)
    ime = bottle.request.forms["ime"]
    id_igre = int(bottle.request.get_cookie("idigre" , secret=SKRIVNOST).split("e")[1])
    imena = []
    igra = golf.igre[id_igre]
    igralci = igra.igralci
    napaka = {}
    for i in igralci:
        imena.append(igralci[i][0].upper())
    if ime.upper() in imena:
        napaka["ime"] = "Ime je že zasedeno"
        return bottle.template("dodajanje-igralcev", igra = igra, igralci=igralci , napaka = napaka)
    elif not ime :
        napaka["ime"] = "Ime mora biti ne prazno"
        return bottle.template("dodajanje-igralcev", igra = igra, igralci=igralci , napaka = napaka)
    elif not ime.isalpha() :
        napaka["ime"] = "Ime je lahko sestavljeno le iz črk"
        return bottle.template("dodajanje-igralcev", igra = igra, igralci=igralci , napaka = napaka)
    else:
        golf.dodaj_igralca(id_igre, ime)
        bottle.redirect("/dodajanje-igralcev/")


@bottle.post("/udarec/")
def udarec():
    golf = model.Golf.nalozi_iz_jsona(model.DATOTEKA_S_STANJEM)
    id_igre = int(bottle.request.get_cookie("idigre" , secret=SKRIVNOST).split("e")[1])
    moc = int(bottle.request.forms["moc"])
    kot = int(bottle.request.forms["kot"])
    preveri = golf.udarec(id_igre, moc, kot)
    if preveri == "Napaka":
        bottle.redirect("/izven-meja/")
    bottle.redirect("/igra")    

@bottle.get("/izven-meja/")
def izven_meja():
    return bottle.template("izven_meja.html")

@bottle.get("/img/<picture>")
def serve_picture(picture):
    return bottle.static_file(picture, root="img")

@bottle.post("/rezultati/")
def rezultati():
    golf = model.Golf.nalozi_iz_jsona(model.DATOTEKA_S_STANJEM)
    golf.nalozi_igre_iz_datoteke()
    id_igre = int(bottle.request.get_cookie("idigre" , secret=SKRIVNOST).split("e")[1])
    igra = golf.igre[id_igre]
    igralci = igra.igralci
    runda = igra.runda
    koncani_igralci = igra.koncani_igralci
    return bottle.template("rezultati.html", igralci = igralci, runda=runda,koncani_igralci=koncani_igralci)

@bottle.get("/navodila/")
def navodila():
    return bottle.template("navodila.html")

bottle.run(reloader=True, debug=True)
