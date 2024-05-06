from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__(shape="square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position, 0)

    def up(self):
        x, y = self.position()
        self.goto(x, y + 40)

    def down(self):
        x, y = self.position()
        self.goto(x, y - 40)
