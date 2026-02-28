# Evaluacion_Contacto_Docente

# 🐍 Proyecto Integrador: Snake Game en Python

**Fecha:** [28/02/2026]
**Estudiante** [David Ganchala]
**Materia:** [Lógica de Programación]
Impacto de las nuevas tecnologías en la sociedad y reflexionen sobre su potencial futuro.

## 1. Introducción al Proyecto y Objetivo
El objetivo de este programa es desarrollar una recreación funcional del clásico juego "Snake" utilizando Python y su librería nativa `turtle`. Este proyecto demuestra la aplicación práctica de los conocimientos adquiridos durante las 4 unidades de la materia, incluyendo el diseño de arquitectura MVC, diagramas funcionales, manejo de estructuras de control lógico (condicionales) y estructuras repetitivas (bucles).

# AUTONOMO 1
1. Diagramas Funcionales: Casos de Uso (UML)
Un Diagrama de Casos de Uso pertenece al estándar UML (Lenguaje Unificado de Modelado). Su objetivo principal no es explicar cómo está programado el software, sino qué hace desde la perspectiva del usuario final.

Para el juego de la Serpiente, los elementos teóricos se definen así:

Actor Principal (El Jugador): Representa a la entidad externa que interactúa con el sistema. En este caso, es la persona sentada frente al teclado.

Límite del Sistema: Es el "cuadro" que engloba todas las funciones. Representa el entorno de ejecución de tu programa en Python.

Casos de Uso (Las funcionalidades):

Inicializar / Reiniciar Partida: El actor interactúa con el menú principal enviando un comando (tecla ESPACIO). El sistema responde cambiando el estado del juego de "Pausa" a "Activo" y reseteando las variables a cero.

Controlar Dirección: El actor ingresa comandos de entrada (W, A, S, D). El sistema procesa estas interrupciones de teclado (eventos) y actualiza el vector de dirección del objeto principal (la cabeza de la serpiente).

Progresar en el Juego (Comer): Este es un caso de uso interno o automático. Cuando el jugador guía la serpiente hacia la coordenada de la comida, el sistema ejecuta una rutina que aumenta el tamaño de la serpiente y reubica la comida aleatoriamente.

Finalizar Partida (Game Over): El sistema evalúa constantemente las reglas físicas. Si el jugador provoca que las coordenadas de la serpiente excedan los límites de la pantalla o coincidan con su propio cuerpo, el sistema detiene la ejecución y muestra el estado final.

2. Arquitectura de Software: Patrón MVC (Modelo-Vista-Controlador)
La arquitectura de software define cómo se organizan los "ladrillos". Elegir el patrón MVC demuestra que no solo escribiste código de arriba hacia abajo, sino que estructuraste el sistema separando las responsabilidades. Esto hace que el código sea escalable y fácil de mantener.

Así es como se desglosa el patrón MVC aplicado específicamente al codigo

El Modelo (M) - La Lógica de Datos:

¿Qué es?: Es el cerebro de los datos. No sabe nada sobre colores, pantallas o teclados; solo maneja información pura y el estado de la aplicación.

Son las variables y listas que declaraste. Por ejemplo, cuerpo = [] (la estructura de datos que guarda el tamaño), las coordenadas x e y, y el estado booleano en_juego = True/False. El Modelo "sabe" dónde está la serpiente, pero no la dibuja.

La Vista (V) - La Interfaz Gráfica (UI):

¿Qué es?: Es la "cara" del programa. Su única responsabilidad es tomar los datos del Modelo y mostrarlos en la pantalla para que el usuario los entienda.

Es todo lo que utiliza la librería turtle. La configuración de ventana.bgcolor("black"), las formas shape("square") o shape("circle"), y los comandos como texto.write(...). La Vista toma las coordenadas que le da el Modelo y pinta los píxeles blancos y rojos en tu monitor.

El Controlador (C) - El Gestor de Reglas:

¿Qué es?: Es el puente de comunicación. Escucha lo que el usuario hace en la Vista, procesa esas acciones, actualiza el Modelo y le dice a la Vista que se actualice.

Son dos partes fundamentales. Primero, el ventana.listen() que captura las teclas (W,A,S,D). Segundo, y más importante, el bucle while True:. Este bucle es el motor de física: calcula distancias (cabeza.distance(comida)), verifica choques contra la pared (cabeza.xcor() > 290) y decide cuándo llamar a la función game_over().

1. Selección del Programa a desarrollar / Generación de Diagramas funcionales y
Arquitectura de Software
1.1. Tipos de Diagramas de funcionalidad y arquitectura de aplicaciones que existen y seleccionar
uno de cada uno.
Diagrama de Funcionalidad (Casos de Uso)
Diagrama de Casos de Uso - Juego la serpiente.

JUGADOR (SERPIENTE).


<img width="507" height="85" alt="image" src="https://github.com/user-attachments/assets/0c79d0dd-cdb1-4ee7-b2cf-c74849944f30" />

SISTEMA, RECORRIDO O MAPA.


<img width="302" height="339" alt="image" src="https://github.com/user-attachments/assets/9d3ac8ed-73b2-4bf8-b5da-4894deaf9de9" />

Sistema del juego

<img width="315" height="326" alt="image" src="https://github.com/user-attachments/assets/8fdb14b2-290c-4259-96e8-7be2cd527617" />

Diagrama de Arquitectura

Arquitectura MVC (Modelo-Vista-Controlador)


<img width="828" height="349" alt="image" src="https://github.com/user-attachments/assets/9bc547f1-048c-4e4b-bdc2-f4d9898a1f86" />

# AUTONOMO 2

DIAGRAMA DE FLUJO DEL JUEGO

<img width="645" height="600" alt="image" src="https://github.com/user-attachments/assets/e40b5223-4576-4a58-8fab-a0e8733b96ef" />
<img width="1132" height="931" alt="image" src="https://github.com/user-attachments/assets/dadf885f-7b1e-4030-b78f-180b00f34313" />
<img width="882" height="906" alt="image" src="https://github.com/user-attachments/assets/cf16cc94-7e31-4f66-b545-10c8be22ff6c" />
<img width="445" height="199" alt="image" src="https://github.com/user-attachments/assets/45f114a0-2ec9-4296-9306-f01cd439b7f5" />



## 2. Explicación de las Principales Funcionalidades
El software cuenta con las siguientes capacidades:
* **Menú Interactivo:** Un estado de pausa inicial que espera la interacción del usuario (tecla ESPACIO) para comenzar.
* **Sistema de Movimiento:** Escucha de eventos de teclado (W, A, S, D) que alteran los vectores de dirección de la "cabeza" de la serpiente.
* **Mecánica de Crecimiento (Comer):** Detección de colisiones mediante cálculo de distancias. Al alcanzar la "comida", se añade un nuevo segmento a la lista que conforma el cuerpo.
* **Física y Colisiones (Game Over):** Evaluaciones lógicas constantes (`if` statements) que detectan si las coordenadas del jugador exceden los límites de la ventana (600x600) o si colisionan con sus propios segmentos.
* ## 3. Explicación de las Principales Funcionalidades y Variables del Sistema

El funcionamiento del juego se sostiene sobre la interacción de diversas variables, objetos y estructuras de datos que conforman el patrón Modelo-Vista-Controlador del software. A continuación, se detallan las variables utilizadas y su propósito en la lógica del juego:

### A. Variables Globales y Estructuras de Datos (El Modelo)
Estas variables almacenan el estado actual de la partida y la información que el programa debe recordar en todo momento.

* **`en_juego` (Booleano):** Es la variable de control (bandera) más importante. Puede ser `True` o `False`. Define si el usuario está en el menú principal/pantalla de Game Over (`False`), o si la partida está en curso y la serpiente puede moverse (`True`). Las funciones de movimiento validan esta variable antes de ejecutarse.
* **`cuerpo` (Lista / Array):** Es una estructura de datos vacía al inicio (`[]`). Almacena secuencialmente los nuevos objetos (segmentos grises) que se crean cada vez que la serpiente come. Su longitud (`len(cuerpo)`) determina el tamaño de la serpiente y se utiliza en bucles `for` para hacer que cada segmento siga al anterior.

### B. Objetos Gráficos e Instancias (La Vista y el Entorno)
Estas variables son instancias de la librería `turtle` y representan los elementos visuales con los que interactúa el usuario.

* **`ventana` (turtle.Screen):** Representa el lienzo o entorno gráfico de 600x600 píxeles. Gestiona el color de fondo, el título y, a través del método `ventana.listen()`, captura los eventos del teclado.
* **`cabeza` (turtle.Turtle):** Es el actor principal controlado por el jugador. Tiene atributos modificados como su forma (`square`), color (`white`) y una propiedad personalizada clave: `cabeza.direction`. Esta última almacena un string ("up", "down", "left", "right", "stop") que le dicta al bucle principal hacia dónde debe calcular la próxima coordenada.
* **`comida` (turtle.Turtle):** Es el objetivo del juego. Es un objeto circular rojo cuyas coordenadas cambian aleatoriamente usando la librería `random` cada vez que el sistema detecta una colisión con la `cabeza`.
* **`texto` (turtle.Turtle):** Un objeto invisible (`hideturtle()`) que se utiliza exclusivamente para renderizar texto en la pantalla, como el menú de inicio ("Presiona ESPACIO") o los mensajes de estado ("¡PERDISTE!").

### C. Variables Locales y Lógica de Funcionamiento (El Controlador)
Dentro de las funciones y del bucle principal (`while True`), se utilizan variables temporales para ejecutar la matemática del juego.

* **`x`, `y` (Enteros/Flotantes):** Variables utilizadas para extraer y modificar las coordenadas en el plano cartesiano. Por ejemplo, al presionar "W", se extrae `cabeza.ycor()` en `y`, se le suman 20 píxeles, y se actualiza la posición con `cabeza.sety(y + 20)`. También se usan para generar las nuevas coordenadas aleatorias de la comida.
* **`nuevo_segmento` (turtle.Turtle):** Variable local que se crea temporalmente dentro de la condición de "Comer". Instancia un nuevo cuadrado gris que inmediatamente es añadido a la lista global `cuerpo` mediante el método `.append()`.
* **`segmento` / `i` (Iteradores):** Utilizados en los bucles `for`. `segmento` se usa para medir la distancia entre la cabeza y cada parte del cuerpo (para detectar choques), mientras que `i` se usa para mover cada bloque del cuerpo a las coordenadas `(x, y)` del bloque que le precede, creando la ilusión de movimiento continuo.

## 3. Instrucciones de Ejecución
 `Juego de la Serpiente.py` 

<img width="748" height="798" alt="image" src="https://github.com/user-attachments/assets/56b1a8dd-c248-4b8b-93b9-731233d7bc39" />

<img width="750" height="780" alt="image" src="https://github.com/user-attachments/assets/c1e6f0b2-19c1-401a-9e91-09119daf5183" />

## PRESENTACION JUEGO DE LA SERPIENTE
[PRESENTACION JUEGO DE LA SERPIENTE.pdf](https://github.com/user-attachments/files/25634368/PRESENTACION.JUEGO.DE.LA.SERPIENTE.pdf)

## VIDEO DEMOSTRATIVO DEL CODIGO Y TODO LO UTILIZADO EN LAS 4 UNIDADES DE LA CLASE 
https://youtu.be/7_OfoeejpLI
