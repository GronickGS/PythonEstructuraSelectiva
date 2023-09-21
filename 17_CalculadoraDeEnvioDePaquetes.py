'''
Calculadora de envío de paquetes:
    Pide al usuario que ingrese el peso y la distancia de envío de un paquete y calcula el costo de envío según una tarifa por peso y distancia.
'''

peso_paquete = float(input("Ingrese el peso del paquete en kilogramos: "))
distancia_envio = float(input("Ingrese la distancia de envío en kilómetros: "))

if peso_paquete <= 5:
    tarifa_peso = 1
elif peso_paquete <= 20:
    tarifa_peso = 2
else:
    tarifa_peso = 3

if distancia_envio <= 100:
    tarifa_distancia = 1
elif distancia_envio <= 500:
    tarifa_distancia = 5
else:
    tarifa_distancia = 10

costo_envio = peso_paquete * tarifa_peso + distancia_envio * tarifa_distancia
print("El costo de envío es:", costo_envio)
