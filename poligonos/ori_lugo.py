from turtle import Turtle, Screen
# Oriana Fatima Lugo Perez
# Ficha: 2878639

# Configurar la pantalla y la tortuga
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("white")
turtle = Turtle()

colours = ["purple","blue", "brown", "orange", "green", "red", "black", "pink"]
def figuras(lado):
    for j in range (3,11): 
        for i in range(j):
            turtle.forward(lado)
            if j==3:
                turtle.left(-120) # Triangulo
                turtle.color(colours[j-3])
            elif j==4:
                turtle.left(-90) # Cuadrado
                turtle.color(colours[j-3])
            elif j==5:
                turtle.left(-72) # Pentagono
                turtle.color(colours[j-3])
            elif j==6:
                turtle.left(-60) # Hexagono
                turtle.color(colours[j-3])
            elif j==7:
                turtle.left(-51.43) # Heptagono
                turtle.color(colours[j-3])
            elif j==8:
                turtle.left(-45) # Octagono
                turtle.color(colours[j-3])
            elif j==9:
                turtle.left(-40) # Nonagono
                turtle.color(colours[j-3])
            elif j==10:
                turtle.left(-36) # Decagono
                turtle.color(colours[j-3])

                
# Ubicar las figuras en la parte superior de la pantalla
turtle.penup()
turtle.goto(0, screen.window_height() / 2 - 50)
turtle.pendown()
                
turtle.speed(2)  # Configurar la velocidad de la tortuga
figuras(100) # llamado de la funcion
screen.mainloop() # Cerrar manualmente 
