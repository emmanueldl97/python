caballero = {"vida":2,"ataque":2,"defensa":2,"alcance":2}
guerrero = {"vida":2,"ataque":2,"defensa":2,"alcance":2}
arquero = {"vida":2,"ataque":2,"defensa":2,"alcance":2}

# cambio en la vida, defensa, alcance y ataque
caballero["vida"]=guerrero["vida"]*2
caballero["defensa"]=guerrero["defensa"]*2

guerrero["ataque"]=caballero["ataque"]*2
guerrero["alcance"]=caballero["alcance"]*2

arquero["ataque"]=guerrero["ataque"]
arquero["vida"]=guerrero["vida"]
arquero["defensa"]=guerrero["defensa"]/2
arquero["alcance"]=guerrero["alcance"]*2

######
print("caballero=", caballero)
print("guerrero=", guerrero)
print("arquero=", arquero)