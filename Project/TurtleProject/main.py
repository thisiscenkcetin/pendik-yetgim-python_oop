import turtle

pencere = turtle.Screen()
pencere.bgcolor("white")
pencere.title("Kare Çizimi")

kalem = turtle.Turtle()
kalem.pensize(3)
kalem.color("blue")

for _ in range(4):
    kalem.forward(100)
    kalem.right(90)


turtle.done()