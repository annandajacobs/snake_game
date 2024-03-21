from turtle import Turtle
ALINHAMENTO = "center"
FONTE = ("Arial", 14, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.ponto_max = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_pontuacao()

    def update_pontuacao(self):
        self.clear()
        self.write(f"Pontuação: {self.score}  Pontuação Máxima: {self.ponto_max}", align=ALINHAMENTO, font=FONTE)

    def reset(self):
        if self.score > self.ponto_max:
            self.ponto_max = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.ponto_max}")
        self.score = 0
        self.update_pontuacao()

    def aumentar_pontuacao(self):
        self.score += 1
        self.clear()
        self.update_pontuacao()

