
distancia = float(input("Ingrese la distancia en kilómetros: "))
peso = float(input("Ingrese el peso del paquete en kilogramos: "))
costo = 0

if distancia <= 100 and peso <= 5:
    costo = 5
elif distancia > 100 and peso <= 5:
    costo = 10
elif distancia <= 100 and peso > 5:
    costo = 8
elif distancia > 100 and peso > 5:
    costo = 15

print("El costo de envío es:", costo, "dólares.")
