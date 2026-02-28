import turtle
import time
import random

# --- 1. CONFIGURACIÓN DE PANTALLA ---
ventana = turtle.Screen()
ventana.title("Juego de la Serpiente - Usa W,A,S,D")
ventana.bgcolor("black")
ventana.setup(width=600, height=600)
ventana.tracer(0) 

# --- 2. OBJETOS DEL JUEGO ---

# La Cabeza
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "stop"

# La Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 100)

# El Texto (Menú y Mensajes)
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 0)

# Variables globales
cuerpo = []
en_juego = False  # Empezamos en el menú, no jugando

# --- 3. FUNCIONES DE MENÚ Y LÓGICA ---

def mostrar_menu():
    texto.clear()
    texto.goto(0, 50)
    texto.write("JUEGO DE LA SERPIENTE", align="center", font=("Courier", 35, "bold"))
    texto.goto(0, -50)
    texto.write("Presiona ESPACIO para Jugar", align="center", font=("Courier", 18, "normal"))
    texto.goto(0, -80)
    texto.write("Usa W, A, S, D para moverte", align="center", font=("Courier", 12, "normal"))

def iniciar_juego():
    global en_juego
    if not en_juego: # Solo inicia si NO estamos jugando ya
        en_juego = True
        texto.clear() # Borrar el menú
        
        # Resetear serpiente
        cabeza.goto(0, 0)
        cabeza.direction = "stop"
        
        # Resetear comida
        comida.goto(0, 100)
        
        # Borrar cuerpo anterior visualmente
        for segmento in cuerpo:
            segmento.goto(1000, 1000)
        cuerpo.clear() # Limpiar la lista

def game_over():
    global en_juego
    en_juego = False
    cabeza.direction = "stop"
    texto.goto(0, 0)
    texto.write("¡PERDISTE!", align="center", font=("Courier", 30, "bold"))
    texto.goto(0, -40)
    texto.write("Presiona ESPACIO para Reiniciar", align="center", font=("Courier", 15, "normal"))

# --- 4. MOVIMIENTO (W, A, S, D) ---

def arriba():
    if en_juego and cabeza.direction != "down":
        cabeza.direction = "up"

def abajo():
    if en_juego and cabeza.direction != "up":
        cabeza.direction = "down"

def izquierda():
    if en_juego and cabeza.direction != "right":
        cabeza.direction = "left"

def derecha():
    if en_juego and cabeza.direction != "left":
        cabeza.direction = "right"

def mover():
    if cabeza.direction == "up":
        cabeza.sety(cabeza.ycor() + 20)
    if cabeza.direction == "down":
        cabeza.sety(cabeza.ycor() - 20)
    if cabeza.direction == "left":
        cabeza.setx(cabeza.xcor() - 20)
    if cabeza.direction == "right":
        cabeza.setx(cabeza.xcor() + 20)

# --- 5. TECLADO ---
ventana.listen()
ventana.onkeypress(arriba, "w")
ventana.onkeypress(abajo, "s")
ventana.onkeypress(izquierda, "a")
ventana.onkeypress(derecha, "d")
ventana.onkeypress(iniciar_juego, "space") # TECLA ESPACIO PARA INICIAR

# --- 6. BUCLE PRINCIPAL ---
mostrar_menu() # Mostrar menú al abrir

while True:
    ventana.update()

    if en_juego:
        # A) Choque con bordes
        if cabeza.xcor() > 290 or cabeza.xcor() < -290 or cabeza.ycor() > 290 or cabeza.ycor() < -290:
            game_over()

        # B) Choque con comida
        if cabeza.distance(comida) < 20:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            comida.goto(x, y)

            nuevo_segmento = turtle.Turtle()
            nuevo_segmento.speed(0)
            nuevo_segmento.shape("square")
            nuevo_segmento.color("grey")
            nuevo_segmento.penup()
            cuerpo.append(nuevo_segmento)

        # C) Mover cuerpo
        for i in range(len(cuerpo) - 1, 0, -1):
            x = cuerpo[i - 1].xcor()
            y = cuerpo[i - 1].ycor()
            cuerpo[i].goto(x, y)

        if len(cuerpo) > 0:
            x = cabeza.xcor()
            y = cabeza.ycor()
            cuerpo[0].goto(x, y)

        mover()

        # D) Choque con propio cuerpo
        for segmento in cuerpo:
            if segmento.distance(cabeza) < 20:
                game_over()

    time.sleep(0.1)