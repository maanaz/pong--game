from turtle import Turtle
import random
import time
class Ball(Turtle):

    def __init__(self) :
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.width(20)
        self.x_move =10
        self.y_move = 10
        self.move_speed = 0.1
        
        self.goto(0,0)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    
    def bounce_y(self):
        self.y_move *= -1
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *=0.9

    def recenter_ball(self):
        
         self.move_speed =0.1
         self.goto(0,0)
         self.bounce_x()
    
        