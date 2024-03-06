from turtle import Turtle
ALINHAMENTO = "center"
FONTE = ("Arial", 14, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_pontuacao()

    def update_pontuacao(self):
        self.write(f"Pontuação: {self.score}", align=ALINHAMENTO, font=FONTE)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALINHAMENTO, font=FONTE)

    def aumentar_pontuacao(self):
        self.score += 1
        self.clear()
        self.update_pontuacao()

