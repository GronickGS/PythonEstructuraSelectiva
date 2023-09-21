'''
Verificación de año bisiesto:
Lee un año ingresado por el usuario y verifica si es un año bisiesto o no.
'''

año = int(input("Ingrese un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(año, "es un año bisiesto.")
else:
    print(año, "no es un año bisiesto.")
