from turtle import Turtle
import random


class Food(Turtle):  # Food class inherits from Turtle superclass

    """It renders itself as a small circle on the screen. Everytime the snake touches
    the food, then the food is going to be placed on a new random location on the screen"""

    def __init__(self):
        """Initializes a new food object"""
        super().__init__()  # allows anything from the superclass to be inherited
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # normally turtle is 20 by 20, but you want 10 by 10(so x 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()  # locates food at a random location in the screen


    def refresh(self):
        """locates food at a new random location in the screen"""
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)  # put food at a random location
