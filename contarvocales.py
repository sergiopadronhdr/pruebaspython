# Ejercicio 9
# Crear una función contar_vocales(), que reciba una palabra y cuente cuantas
# letras "a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
# Se puede hacer que el usuario sea quien elija la palabra.

def contar_vocales(palabra):
    print("La palabra " + palabra + " contiene " + str(palabra.count("a")) + " a")
    print("La palabra " + palabra + " contiene " + str(palabra.count("A")) + " A")
    print("La palabra " + palabra + " contiene " + str(palabra.count("e")) + " e")
    print("La palabra " + palabra + " contiene " + str(palabra.count("E")) + " E")
    print("La palabra " + palabra + " contiene " + str(palabra.count("i")) + " i")
    print("La palabra " + palabra + " contiene " + str(palabra.count("I")) + " I")
    print("La palabra " + palabra + " contiene " + str(palabra.count("o")) + " o")
    print("La palabra " + palabra + " contiene " + str(palabra.count("O")) + " O")
    print("La palabra " + palabra + " contiene " + str(palabra.count("u")) + " u")
    print("La palabra " + palabra + " contiene " + str(palabra.count("U")) + " U")

palabra = input("Introduzca una palabra: ")
contar_vocales(palabra)