# we mar 9, we mar 10, su mar 13 and mo mar 14, we mar 23, th mar 24, 2022
# day 20 - the snake game - part 1
# day 21 - the snake game - part 2
# day 24 - the snake game - better version
# OBJECTIVE: Create the Nokia snake game

"""main.py controls the entire game: dictates how the screen should behave, how the snake behaves"""

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time  # this time module will help to slow down what is happening

# create screen and adjust its appearance:
screen = Screen()
screen.setup(width=600, height=600)  # set the screens sizes
screen.bgcolor("black")  # set the screens background color
screen.title("Snake Game")  # set the title at the top of the screen
# make the snake move smoothly as one piece:
screen.tracer(0)  # turns tracer off -> now screen.update() can be used to tell the program when to refresh the screen
# without screen.update() we will only see a black screen

snake = Snake()
snake.speed("fastest")

# ToDo 4a: Put food (a blue circle) on the screen and detect collision of the food
food = Food()
scoreboard = Score()

# ToDo 3: CONTROL THE SNAKE
screen.listen()  # start listening for keystrokes
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

# ToDo 2: MOVE THE SNAKE
game_is_on = True
while game_is_on:
    screen.update()  # refresh the screen
    time.sleep(0.1)  # delay for 0.1 second
    snake.move()

    # ToDo 4b: DETECT COLLISION WITH FOOD
    # 1) snake hits a piece of food
    # 2) everytime snake touches the food, food moves to a random location on the screen
    # detect collision with food:
    head = snake.all_segments[0]
    if head.distance(food) < 15:  # food is 10 by 10 so distance of 15 works good
        food.refresh()  # refresh foods location
        snake.extend()
        scoreboard.update_score()

    # detect collision with wall:
    if head.xcor() > 280 or head.xcor() < -290 or head.ycor() > 280 or head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        game_is_on=False

# make code above shorter by using slicing:
    for segment in snake.all_segments[1:]:  # all segments except the head
        if head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            is_game_on=False

screen.exitonclick()  # screen only disappears when you click











