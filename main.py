from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
# Tracer is going to help us set the time when the screen should update what our snake does, to give it a smooth animation
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    print()

    # Detect collision with food

    if snake.segments[0].distance(food) < 15:
        food.refresh()

screen.exitonclick()
