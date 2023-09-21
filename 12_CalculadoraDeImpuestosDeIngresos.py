'''
Calculadora de impuestos de ingresos:
    Pide al usuario que ingrese su ingreso anual y calcula el impuesto a pagar según un sistema de impuestos progresivos.
'''

ingreso_anual = float(input("Ingrese su ingreso anual: "))

if ingreso_anual <= 10000:
    impuesto = ingreso_anual * 0.1
elif ingreso_anual <= 50000:
    impuesto = 1000 + (ingreso_anual - 10000) * 0.2
else:
    impuesto = 9000 + (ingreso_anual - 50000) * 0.3

print("El impuesto a pagar es:", impuesto)
