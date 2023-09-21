'''
Ordenar tres números:
Pide al usuario que ingrese tres números y muestra los números en orden ascendente.
'''

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

if numero1 <= numero2 <= numero3:
    print("Los números en orden ascendente son:", numero1, numero2, numero3)
elif numero1 <= numero3 <= numero2:
    print("Los números en orden ascendente son:", numero1, numero3, numero2)
elif numero2 <= numero1 <= numero3:
    print("Los números en orden ascendente son:", numero2, numero1, numero3)
elif numero2 <= numero3 <= numero1:
    print("Los números en orden ascendente son:", numero2, numero3, numero1)
elif numero3 <= numero1 <= numero2:
    print("Los números en orden ascendente son:", numero3, numero1, numero2)
else:
    print("Los números en orden ascendente son:", numero3, numero2, numero1)
