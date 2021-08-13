import bottle
import model

@bottle.get("/")
def osnovna_stran():
    return bottle.template("osnovna.html")

@bottle.get("/igra")
def igra_stran():
    slovar = {}
    seznam_igralcev = model.igralci
    for i in seznam_igralcev:
        igralec = model.igralci[i]
        koordinate = model.igralci[i][1]
        x_koordinata, y_koordinata = koordinate
        slovar[igralec] = koordinate
    return bottle.template("igra.html", slovar, seznam_igralcev, igralec, koordinate, x_koordinata, y_koordinata )

bottle.run(reloader=True, debug=True)