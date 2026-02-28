print("Piensa en un número del 1 al 20 y yo lo adivinaré.")
input("Presiona Enter cuando estés listo...")

minimo = 1
maximo = 20
intentos = 10
encontrado = False

while not encontrado:
    intento = (minimo + maximo) // 2
    intentos += 1
    print(f"¿Es {intento} tu número?")
    respuesta = input("Escribe 'mayor', 'menor' o 'correcto': ").lower()

    if respuesta == "mayor":
        minimo = intento + 1
    elif respuesta == "menor":
        maximo = intento - 1
    elif respuesta == "correcto":
        encontrado = True
        print(f"¡Adiviné tu número en {intentos} intento(s)!")
    else:
        print("Respuesta no válida. Por favor escribe 'mayor', 'menor' o 'correcto'.")
