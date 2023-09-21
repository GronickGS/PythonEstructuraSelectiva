'''
Cálculo del salario según el nivel de empleado:
    Solicita al usuario que ingrese su nivel de empleado (1, 2 o 3) y 
    las horas trabajadas en la semana. Calcula y muestra el salario, 
    considerando diferentes tarifas por hora para cada nivel de empleado.
'''
nivel_empleado = int(input("Ingrese su nivel de empleado (1, 2 o 3): "))
horas_trabajadas = float(input("Ingrese las horas trabajadas en la semana: "))

if nivel_empleado == 1:
    salario = horas_trabajadas * 15
elif nivel_empleado == 2:
    salario = horas_trabajadas * 20
elif nivel_empleado == 3:
    salario = horas_trabajadas * 25
else:
    salario = 0

print("Su salario es:", salario)
