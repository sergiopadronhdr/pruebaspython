def calcular_capital(capital,porcent,years):
    final = capital * ((1 + (porcent/100)) ** years)
    print(final)

capital = int(input("Indique el capital inicial: "))
porcent = float(input("Indique la tasa de interés: "))
years = int(input("Indique el número de años: "))
calcular_capital(capital, porcent, years)