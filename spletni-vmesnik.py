import bottle
import model
SKRIVNOST = "skrivnost je skrivnost"

golf = model.Golf(model.DATOTEKA_S_STANJEM)

@bottle.get("/")
def osnovna_stran():
    return bottle.template("osnovna.html")

#@bottle.get("/igra")
#def igra_stran():
#    slovar = {}
#    slovar_igralcev = nova_igra.igralci
#    for i in slovar_igralcev:
#        x_koordinata_luknje, y_koordinata_luknje = nova_igra.pozicija_luknje
#        koordinate = slovar_igralcev[i][1]
#        x_koordinata, y_koordinata = koordinate
#        slovar[i] = koordinate
#    return bottle.template("igra.html", slovar = slovar_igralcev ,x_koordinata_luknje =x_koordinata_luknje, y_koordinata_luknje = y_koordinata_luknje)

@bottle.post("/nova-igra/")
def preusmeritev_na_izbiro_igre():
    bottle.redirect("/izbira-igre/")

@bottle.get("/izbira-igre/")
def izibra_igre():
    return bottle.template("izbira.html")

@bottle.post("/izbrana-igra/1")
def ena():
    id_igre = golf.nova_igra(1)
    bottle.response.set_cookie("idigre" , "idigre{}".format(id_igre), path="/" , secret = SKRIVNOST )
    bottle.redirect("/dodajanje-igralcev/")

@bottle.post("/izbrana-igra/2")
def dva():
    id_igre = golf.nova_igra(2)
    bottle.response.set_cookie("idigre" , "idigre{}".format(id_igre), path="/" , secret = SKRIVNOST )
    bottle.redirect("/dodajanje-igralcev/")

@bottle.post("/izbrana-igra/3")
def tri():
    id_igre = golf.nova_igra(3)
    bottle.response.set_cookie("idigre" , "idigre{}".format(id_igre), path="/" , secret = SKRIVNOST )
    bottle.redirect("/dodajanje-igralcev/")

@bottle.post("/izbrana-igra/4")
def stiri():
    id_igre = golf.nova_igra(4)
    bottle.response.set_cookie("idigre" , "idigre{}".format(id_igre), path="/" , secret = SKRIVNOST )
    bottle.redirect("/dodajanje-igralcev/")

@bottle.post("/izbrana-igra/5")
def pet():
    id_igre = golf.nova_igra(5)
    bottle.response.set_cookie("idigre" , "idigre{}".format(id_igre), path="/" , secret = SKRIVNOST )
    bottle.redirect("/dodajanje-igralcev/")

@bottle.get("/dodajanje-igralcev/")
def stran_dodajanja():
    return bottle.template("dodajanje-igralcev.html")

@bottle.post("/dodaj-igralca/")
def dodaj_igralca():
    ime = bottle.request.forms["ime"]
    if ime:
        golf.dodaj_igralca(ime)
    else:
        return "ime mora biti ne prazno"
@bottle.post("/udarec/")
def udarec():
    moc = int(bottle.request.forms["moc"])
    kot = int(bottle.request.forms["kot"])
    golf.udarec(moc,kot)
    bottle.redirect("/igra")

@bottle.get("/img/<picture>")
def serve_picture(picture):
    return bottle.static_file(picture, root="img")


bottle.run(reloader=True, debug=True)