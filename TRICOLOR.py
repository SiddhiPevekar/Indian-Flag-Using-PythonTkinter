import time
import turtle
import winsound


from turtle import Turtle
from random import randint

#window screen
window= turtle.Screen()
window.title("tricolor")
window.bgcolor("#b3daff")

india=Turtle()
india.color("red")
india.speed(10)
india.shape("turtle")             
india.penup()
india.setpos(-100,200)
india.write("MY PRIDE!",font=("Arial",30,"bold","underline"))
india.penup()
india.hideturtle()
india.pendown()

soldier=Turtle()
soldier.speed(100)
soldier.shape("turtle")
soldier.penup()
flag_height=300
flag_width=450
start_x=-225
start_y=150
stripe_height= flag_height/3
stripe_width= flag_width
chakra_radius= stripe_height/2

def draw_fill_rectangle(x, y, height, width, color):
    soldier.goto(x,y)
    soldier.pendown()
    soldier.color(color)
    soldier.begin_fill()
    soldier.forward(width)
    soldier.right(90)
    soldier.forward(height)
    soldier.right(90)
    soldier.forward(width)
    soldier.right(90)
    soldier.forward(height)
    soldier.right(90)
    soldier.end_fill()
    soldier.penup()
    

 
def draw_stripes():
    x=start_x
    y=start_y
    draw_fill_rectangle(x, y, stripe_height, stripe_width, "orange")
    y= y - stripe_height
    draw_fill_rectangle(x, y, stripe_height, stripe_width, "white")
    y= y - stripe_height
    draw_fill_rectangle(x, y, stripe_height, stripe_width, "green")
    y= y - stripe_height
soldier.hideturtle()

def draw_chakra():
    farmer=turtle.Turtle()
    farmer.speed(100)
    
    for i in range(24):
        farmer.forward(50)
        farmer.penup()
        farmer.setposition(0,0)
        farmer.right(15)
        farmer.pendown()
    
    
    farmer.setposition(0,0-chakra_radius)
    farmer.circle(chakra_radius)
    farmer.penup()
    farmer.hideturtle()
    
    
time.sleep(0)
draw_stripes()
draw_chakra()
soldier.hideturtle()


winsound.PlaySound("C:/Users/HP/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.8/jan.wav",winsound.SND_FILENAME)
                 
turtle.done()    
   
