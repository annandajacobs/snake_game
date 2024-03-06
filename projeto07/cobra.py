from turtle import Turtle
POSICAO_INICIAL = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Cobra:
    def __init__(self):
        self.passos = []
        self.criar_cobra()
        self.head = self.passos[0]

    def criar_cobra(self):
        for posicao in POSICAO_INICIAL:
            self.adc_segmentos(posicao)

    def adc_segmentos(self, posicao):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(posicao)
        self.passos.append(snake)

    def extender(self):
        #adicionar um novo segmento a cobra
        self.adc_segmentos(self.passos[-1].position()) #está adicionando mais um segmento na última posição

    def move(self):
        for num_passos in range(len(self.passos) - 1, 0, -1):
            novo_x = self.passos[num_passos - 1].xcor()
            novo_y = self.passos[num_passos - 1].ycor()
            self.passos[num_passos].goto(novo_x, novo_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
