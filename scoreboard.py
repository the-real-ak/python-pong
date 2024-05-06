from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(shape="turtle", visible=False)
        self.color("white")
        self.penup()
        self.goto(0, 190)
        self.player1_score = 0
        self.player2_score = 0
        self.register_board()

    def register_board(self):
        self.clear()
        self.write(f"{self.player1_score} {self.player2_score}", align=ALIGNMENT, font=FONT)

    def increment_player1(self):
        self.player1_score += 1
        self.register_board()

    def increment_player2(self):
        self.player2_score += 1
        self.register_board()
