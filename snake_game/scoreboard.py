from turtle import Turtle

# constant variables:
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")  # Courier is a good video game letter type

class Score(Turtle):  # Score inherits from Turtle superclass
    """a turtle that keeps track of the score and displays the score in the program"""

    def __init__(self):
        """initializes a new scoreboard object"""
        super().__init__()  # score inherits from Turtle superclass
        self.score = 0
        self.display_score()
        self.high_score=0
    def display_score(self):
        """displaying sum of points at the top of the screen"""
        self.clear()
        self.goto(0, 260)  # put text at the bottom of the screen
        self.hideturtle()  # hide turtle, otherwise you see turtle below the text
        self.color("white")
        with open("data.txt", mode="r") as data:
            high_score = int(data.read())
        self.write(f"SCORE = {self.score} High Score: {high_score} ", align=ALIGNMENT, font=FONT)

    def reset(self):
        with open("data.txt", mode="r") as data:
            high_score = int(data.read())
            if self.score >= high_score:
                with open("data.txt", mode="w") as data:
                    self.score = str(self.score)
                    data.write(self.score)
        self.score = 0
        self.display_score()

    def update_score(self):
        """adds a point to the score and display new score"""
        self.score += 1
        self.clear()
        self.display_score()