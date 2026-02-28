# Evaluacion_Contacto_Docente

# 🐍 Proyecto Integrador: Snake Game en Python

**Fecha:** [28/02/2026]
**Estudiante** [David Ganchala]
**Materia:** [Lógica de Programación]
Impacto de las nuevas tecnologías en la sociedad y reflexionen sobre su potencial futuro.

## 1. Introducción al Proyecto y Objetivo
El objetivo de este programa es desarrollar una recreación funcional del clásico juego "Snake" utilizando Python y su librería nativa `turtle`. Este proyecto demuestra la aplicación práctica de los conocimientos adquiridos durante las 4 unidades de la materia, incluyendo el diseño de arquitectura MVC, diagramas funcionales, manejo de estructuras de control lógico (condicionales) y estructuras repetitivas (bucles).

# AUTONOMO 1
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

<img width="748" height="798" alt="image" src="https://github.com/user-attachments/assets/56b1a8dd-c248-4b8b-93b9-731233d7bc39" />

<img width="750" height="780" alt="image" src="https://github.com/user-attachments/assets/c1e6f0b2-19c1-401a-9e91-09119daf5183" />

