# Ejercicio 1
# Escriba una función que tome una lista de números y devuelva la suma acumulada, es decir,
# una nueva lista donde el primer elemento es el mismo, el segundo elemento es la suma del
# primero con el segundo, el tercer elemento es la suma del resultado anterior con el siguiente
# elemento y así sucesivamente. Por ejemplo, la suma acumulada de [1,2,3] es [1, 3, 6].

def lista_suma_acumulada(lista):
    suma = 0
    for i in lista:
        suma = suma + i
        print(suma)
def introducir_lista(lista):
    for i in range(3):
        valor = int(input("Introduzca un valor entero: "))
        lista.append(valor)
lista = []
introducir_lista(lista)
lista_suma_acumulada(lista)

# Ejercicio 2
# Escribe una función llamada "elimina" que tome una lista y elimine el primer y último
# elemento de la lista y cree una nueva lista con los elementos que no fueron eliminados.
# Luego escribe una función que se llame "media" que tome una lista y devuelva una nueva
# lista que contenga todos los elementos de la lista anterior menos el primero y el último.

def introducir_lista(lista):
    for i in range(5):
        valor = int(input("Introduzca un valor entero: "))
        lista.append(valor)
def elimina(lista):
    lista.pop()
    lista.pop(0)
    lista_nueva = []
    lista_nueva = lista
def media(lista):
    lista.pop()
    lista.pop(0)
    lista_nueva = []
    lista_nueva = lista
    print(lista_nueva)
lista = []
introducir_lista(lista)
elimina(lista)
media(lista)
# Ejercicio 3
# Escribe una función "ordenada" que tome una lista como parámetro y devuelva True si la lista
# está ordenada en orden ascendente y devuelva False en caso contrario.
# Por ejemplo, ordenada([1, 2, 3]) retorna True y ordenada([b, a]) retorna False.

def ordenada(lista):
    lista_nueva = lista.copy()
    lista_nueva.sort()
    if lista_nueva == lista:
        return True
    else:
        return False
def introducir_lista(lista):
    for i in range(5):
        valor = int(input("Introduzca un valor entero: "))
        lista.append(valor)
lista = []
introducir_lista(lista)
ordenada(lista)