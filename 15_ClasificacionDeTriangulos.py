'''
Clasificación de triángulos:
    Pide al usuario que ingrese las longitudes de tres lados de un triángulo
    y clasifica el triángulo según sus lados (equilátero, isósceles o escaleno)
    y según sus ángulos (rectángulo, obtuso o agudo).
'''
lado1 = float(input("Ingrese la longitud del primer lado: "))
lado2 = float(input("Ingrese la longitud del segundo lado: "))
lado3 = float(input("Ingrese la longitud del tercer lado: "))

# Clasificación por lados
if lado1 == lado2 == lado3:
    tipo_lados = "equilátero"
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    tipo_lados = "isósceles"
else:
    tipo_lados = "escaleno"

# Clasificación por ángulos
lados_ordenados = sorted([lado1, lado2, lado3])
a, b, c = lados_ordenados
if a**2 + b**2 == c**2:
    tipo_angulos = "rectángulo"
elif a**2 + b**2 < c**2:
    tipo_angulos = "obtuso"
else:
    tipo_angulos = "agudo"

print("El triángulo es", tipo_lados, "y", tipo_angulos)

