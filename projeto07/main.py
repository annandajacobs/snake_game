from turtle import Screen
from cobra import Cobra
from comida import Food
from scoreboard import Scoreboard
import time

tela = Screen()
tela.setup(width=600, height=600)
tela.bgcolor("black")
tela.title("My Snake Game")
tela.tracer(0)

posicoes = [0 ,-20, -40]
passos = []

cobra = Cobra()
comida = Food()
scoreboard = Scoreboard()

tela.listen()
tela.onkey(cobra.up, "Up")
tela.onkey(cobra.down, "Down")
tela.onkey(cobra.left, "Left")
tela.onkey(cobra.right, "Right")

game_is_on = True
while game_is_on:
    tela.update()
    time.sleep(0.1)
    cobra.move()

    #detectar colisão com comida
    if cobra.head.distance(comida) < 15:
        comida.refresh()
        cobra.extender()
        scoreboard.aumentar_pontuacao()

    #detectar colisão com a parede.
    if cobra.head.xcor() > 280 or cobra.head.xcor() < -280 or cobra.head.ycor() > 280 or cobra.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    #detectar colisão com a calda. (se a cabeça colidir com qualquer segmento da cobra, então game_over)
    for segmentos in cobra.passos[1:]:
        if cobra.head.distance(segmentos) < 10:
            game_is_on = False 
            scoreboard.game_over()

tela.exitonclick()
