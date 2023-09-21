'''
Calculadora de descuento de compra:
    Pide al usuario que ingrese el precio de un artículo y su código de descuento (si lo tiene) y calcula el precio final después del descuento.
'''

precio = float(input("Ingrese el precio del artículo: "))
codigo_descuento = input("Ingrese el código de descuento (si tiene): ")

if codigo_descuento == "DESC10":
    descuento = precio * 0.1
elif codigo_descuento == "DESC20":
    descuento = precio * 0.2
else:
    descuento = 0

precio_final = precio - descuento
print("El precio final después del descuento es:", precio_final)
