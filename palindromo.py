# 7 - Definir una función es_palindromo() que reconoce palíndromos
# (es decir, palabras que tienen el mismo aspecto escritas invertidas),
# ejemplo: es_palindromo ("radar") tendría que devolver True.

def es_palindromo(palabra):
    palabrainvertida = palabra[::-1]
    if palabra == palabrainvertida:
        print("La palabra " + palabra + " es palíndromo")
    else:
        print("La palabra " + palabra + " NO es palíndromo")

palabra = input("Introduzca una palabra: ")
es_palindromo(palabra)