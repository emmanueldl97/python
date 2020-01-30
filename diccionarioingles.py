#diccionario de español a ingles
while True:
    diccionario = {"azul": "blue", "rojo": "red", "amarillo": "yellow", "verde": "green", "gris": "gray",
                   "negro": "black", "blanco": "white", }
    diccionario["anaranjado"] = "orange"
    diccionario["hola"] = "hello"
    diccionario["amigo"] = "friend"
    diccionario["caliente"] = "hot"
    diccionario["cama"] = "bed"
    diccionario["silla"] = "chair"
    diccionario["cojin"] = "pillow"
    diccionario["pets"] = "mascotas"
    diccionario["amor"] = "love"
    diccionario["zapatos"] = "shooes"
    diccionario["espejo"] = "mirrow"
    diccionario["casa"] = "house"
    diccionario["escuela"] = "school"
    diccionario["labios"] = "lip"
    diccionario["naris"] = "nose"
    diccionario["botella"] = "botle"
    diccionario["agua"] = "water"
    diccionario["ojos"] = "eyes"

    a = input(" presiona 0 para salir\n ingresa la palabra a traducir:")
    if a=='0':
        print("vuelva pronto")
        break
    else:
        print(diccionario[a])