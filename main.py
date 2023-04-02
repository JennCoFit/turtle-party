# Turtle Party Project
# by Jennifer Connor
# April 2, 2023
import turtle
turtle.color("red")

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
  
# forward helper function
def move(len):
  back(-1 * len)
    
def polygon(num, size):
  for i in range(num):
    turtle.forward(size)
    turtle.left(360 / num)
    
def spiral(len, angle):
  for i in range(len, 5, -5):
    turtle.forward(i)
    turtle.right(angle)

spiral(75, 45)
move(150)
turtle.color("blue")
spiral(100, 90)
