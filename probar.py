

import json

with open('lab4Hab.json', 'r') as archivo:
    datos = json.load(archivo)
    print(f"Tipo de laberinto: {type(datos)}")
    print(f"Tipo de laberinto: {type(datos.get('laberinto'))}")
    print(f"Tipo de laberinto: {type(datos.get('laberinto')[0])}")
    print(f"Tipo de laberinto: {type(datos.get('laberinto')[0].get('tipo'))}")