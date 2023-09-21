'''
Simulador de piedra, papel y tijeras:
    Juega contra la computadora en una versión de piedra, papel y tijeras. Solicita al usuario que elija su jugada y luego genera una jugada aleatoria para la computadora.
'''

import random

jugada_usuario = input("Elige tu jugada (piedra, papel o tijeras): ")
jugada_computadora = random.choice(["piedra", "papel", "tijeras"])

print("La computadora eligió:", jugada_computadora)

if jugada_usuario == jugada_computadora:
    resultado = "Empate"
elif (jugada_usuario == "piedra" and jugada_computadora == "tijeras") or (jugada_usuario == "papel" and jugada_computadora == "piedra") or (jugada_usuario == "tijeras" and jugada_computadora == "papel"):
    resultado = "Ganaste"
else:
    resultado = "La computadora ganó"

print("Resultado:", resultado)
