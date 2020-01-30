while True:
    consulta=int(input("1) Consultar \n 2) Salir"))
    if consulta==1:
        nombre=input("ingresa tu nombre")
        sexo=input("sexo? M\F")
        if sexo !='m' or sexo !='f':
            print("error de sexo")
        print(f"hola {nombre} eres del sexo {sexo}")
    elif consulta==2:
        print("cerrando programa")
        break
    else:
        print("opcion no reconocida")

