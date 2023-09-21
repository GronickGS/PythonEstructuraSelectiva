'''
Juego de adivinar el número secreto:
    Genera un número secreto aleatorio entre 1 y 100. Luego, permite al usuario adivinar el número secreto con un número limitado de intentos.
'''
import random

numero_secreto = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input("Intenta adivinar el número secreto (entre 1 y 100): "))
    intentos += 1

    if intento == numero_secreto:
        print("¡Felicidades! Adivinaste el número en", intentos, "intentos.")
        break
    elif intento < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
