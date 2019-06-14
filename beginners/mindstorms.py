import turtle as t

def draw_square(some_t):
    for i in range(4):
        some_t.forward(100)
        some_t.right(90)

def draw_art():
    window = t.Screen()
    window.bgcolor('red')

    brad = t.Turtle()
    brad.shape('turtle')
    brad.color("yellow")
    brad.speed(0) #fastest

    for i in range(72):
        draw_square(brad)
        brad.right(5)

    window.exitonclick()

draw_art()