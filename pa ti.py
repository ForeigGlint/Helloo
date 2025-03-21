from turtle import *
import colorsys
import math

# Configuración inicial
speed(0.25)
bgcolor("black")
title("Flor para ti")

# Crear tortuga para el mensaje
mensaje = Turtle()
mensaje.hideturtle()
mensaje.penup()
mensaje.goto(0, 300)
mensaje.color("#39FF14")  # Verde fluorescente
mensaje.write("ESTA FLOR ES PARA TI\nNO ES MUCHO PERO ES PARA TI", 
             align="center", 
             font=("Arial", 20, "bold"))

# Tortuga para dibujar la flor
flor = Turtle()
flor.speed(0)
flor.hideturtle()

# Genera los pétalos
flor.goto(0, -40)
h = 0

for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(0.125, 1, 1)
        flor.color(c)
        flor.rt(90)
        flor.circle(150-j*6, 90)
        flor.lt(90)
        flor.circle(150-j*6, 90)
        flor.rt(180)
    flor.circle(40, 24)

# Genera el centro de la flor
flor.color("black")
flor.shape("turtle")
flor.fillcolor("brown")
phi = 137.508 * (math.pi/180.0)

for i in range(200):
    r = 4 * math.sqrt(i)
    theta = i*phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    flor.penup()
    flor.goto(x, y)
    flor.setheading(i * 137.508)
    flor.pendown()
    flor.stamp()

done()