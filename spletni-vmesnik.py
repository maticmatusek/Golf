import bottle
import model
SKRIVNOST = "skrivnost je skrivnost"

golf = model.Golf(model.DATOTEKA_S_STANJEM)


@bottle.get("/")
def osnovna_stran():
    return bottle.template("osnovna.html")

@bottle.get("/igra")
def igra_stran():
    golf.nalozi_igre_iz_datoteke()
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


@bottle.post("/nova-igra/")
def preusmeritev_na_izbiro_igre():
    bottle.redirect("/izbira-igre/")


@bottle.get("/izbira-igre/")
def izibra_igre():
    return bottle.template("izbira.html")


@bottle.post("/izbrana-igra/1")
def ena():
    id_igre = golf.nova_igra(1)
    bottle.response.set_cookie("idigre", "idigre{}".format(
        id_igre), path="/", secret=SKRIVNOST)
    bottle.redirect("/dodajanje-igralcev/")


@bottle.post("/izbrana-igra/2")
def dva():
    id_igre = golf.nova_igra(2)
    bottle.response.set_cookie("idigre", "idigre{}".format(
        id_igre), path="/", secret=SKRIVNOST)
    bottle.redirect("/dodajanje-igralcev/")


@bottle.post("/izbrana-igra/3")
def tri():
    id_igre = golf.nova_igra(3)
    bottle.response.set_cookie("idigre", "idigre{}".format(
        id_igre), path="/", secret=SKRIVNOST)
    bottle.redirect("/dodajanje-igralcev/")


@bottle.post("/izbrana-igra/4")
def stiri():
    id_igre = golf.nova_igra(4)
    bottle.response.set_cookie("idigre", "idigre{}".format(
        id_igre), path="/", secret=SKRIVNOST)
    bottle.redirect("/dodajanje-igralcev/")


@bottle.post("/izbrana-igra/5")
def pet():
    id_igre = golf.nova_igra(5)
    bottle.response.set_cookie("idigre", "idigre{}".format(
        id_igre), path="/", secret=SKRIVNOST)
    bottle.redirect("/dodajanje-igralcev/")


@bottle.post("/izbrana-igra/6")
def random():
    id_igre = golf.nova_igra()
    bottle.response.set_cookie("idigre", "idigre{}".format(
        id_igre), path="/", secret=SKRIVNOST)
    bottle.redirect("/dodajanje-igralcev/")


@bottle.get("/dodajanje-igralcev/")
def stran_dodajanja():
    id_igre = int(bottle.request.get_cookie("idigre" , secret=SKRIVNOST).split("e")[1])
    igra = golf.igre[id_igre]
    igralci = igra.igralci
    return bottle.template("dodajanje-igralcev.html", igra = igra, igralci = igralci)


@bottle.post("/dodaj-igralca/")
def dodaj_igralca():
    ime = bottle.request.forms["ime"]
    id_igre = int(bottle.request.get_cookie("idigre" , secret=SKRIVNOST).split("e")[1])
    if ime:
        golf.dodaj_igralca(id_igre, ime)
    else:
        return "ime mora biti ne prazno"
    bottle.redirect("/dodajanje-igralcev/")


@bottle.post("/udarec/")
def udarec():
    id_igre = int(bottle.request.get_cookie("idigre" , secret=SKRIVNOST).split("e")[1])
    moc = int(bottle.request.forms["moc"])
    kot = int(bottle.request.forms["kot"])
    golf.udarec(id_igre, moc, kot)
    bottle.redirect("/igra")


@bottle.get("/img/<picture>")
def serve_picture(picture):
    return bottle.static_file(picture, root="img")

@bottle.post("/rezultati/")
def rezultati():
    golf.nalozi_igre_iz_datoteke()
    id_igre = int(bottle.request.get_cookie("idigre" , secret=SKRIVNOST).split("e")[1])
    igra = golf.igre[id_igre]
    igralci = igra.igralci
    x_koordinata_luknje, y_koordinata_luknje = igra.pozicija_luknje
    pozicija_luknje = igra.pozicija_luknje
    igralec_na_vrsti = igra.igralec_na_vrsti
    koordinate_zacetka = igra.koordinate_zacetka
    runda = igra.runda
    koncani_igralci = igra.koncani_igralci
    return bottle.template("rezultati.html", igralci = igralci, runda=runda,koncani_igralci=koncani_igralci)

bottle.run(reloader=True, debug=True)
