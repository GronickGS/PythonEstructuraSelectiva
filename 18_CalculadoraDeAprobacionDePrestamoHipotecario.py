'''
Calculadora de aprobación de préstamo hipotecario:
    Pide al usuario que ingrese su salario anual, el monto del préstamo hipotecario y la tasa de interés. Luego, verifica si es elegible para un préstamo hipotecario según su salario y la tasa de interés.
'''

salario_anual = float(input("Ingrese su salario anual: "))
monto_prestamo = float(input("Ingrese el monto del préstamo hipotecario: "))
tasa_interes = float(input("Ingrese la tasa de interés del préstamo (%): "))

if salario_anual * 0.28 >= monto_prestamo * (tasa_interes / 100) * (1 + (tasa_interes / 100)) ** 30 / ((1 + (tasa_interes / 100)) ** 30 - 1):
    elegible = True
else:
    elegible = False

if elegible:
    print("¡Eres elegible para el préstamo hipotecario!")
else:
    print("No eres elegible para el préstamo hipotecario.")
