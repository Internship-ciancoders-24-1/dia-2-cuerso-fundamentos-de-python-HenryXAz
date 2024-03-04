import copy

countries = ['Mexico', 'Guatemala', 'Argentina', 'Colombia']

# a pesar de tener los mismos valores, se almacenan en diferentes direcciones de memoria
ages = [12, 18, 24, 34, 50]

weights  = [12, 18, 24, 34, 50]

countries[0] = 'Ecuador' # las listas pueden ser modificadas a diferencia de los string

global_countries = countries # no se clona la lista, solo se hace referencia a la direccion de memoria

clone_countries = copy.copy(countries) # se hace una copia de la lista

# recorrer la lista con for
for country in countries:
    print(country)



