
monto_total = float(input("Ingrese el monto total de la compra: "))
if monto_total >= 100:
    descuento = 0.1 * monto_total
else:
    descuento = 0
monto_final = monto_total - descuento
print("Monto a pagar con descuento:", monto_final)
