 # se puede inicializar de dos formas:
productos = {
    "jugo" : "de naranja",
    "pastel" : "de chocolate"
}
productos = dict()

# para poder recorrer un diccionario se pude realizar lo siguiente:

# imprime las llaves del diccionario
for key in productos.key():
    print(key)

#  imprime los valores del diccionario
for value in productos.values():
    print(value)

# imprimir clave y valor del diccionario
for key, value in productos.items():
    print(key, value)