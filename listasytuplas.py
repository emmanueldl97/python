
#Listas
lista=[1,2,"hola",3.2,True,False,1]

print(lista)
print(f"la cantidad de datos almacenados en la lista es de: {len(lista)}")
# agrega dato a la lista
lista.append("kpedo")
# agrega dado indicandole el numero de posición
lista.insert(2,"jejeje")
print(f"lista actializada{lista}")
print("####################################")

#Tuplas
tupla=(1,3,"hola",1,4.3,"amigo")
print(tupla)
print(f"La cantidad de datos almacenados en la tupla es de: {tupla.__len__()}")
print(f"la cantidad de holas almacenados en la tupla es de: {tupla.count('hola') } ")
print(f"Hola se encuentra en la posicion: {tupla.index('hola')}")