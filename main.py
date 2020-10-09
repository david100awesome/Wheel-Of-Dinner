from turtle import *
import random

setup()

t1 = Turtle()

colors = ["red", "blue", "green", "yellow", "purple", "orange"]

t1.up()

t1.goto(-200, 0)

t1.down()

t1.width(5)

t1.hideturtle()

t1.speed(0)

red = 0
blue = 0
green = 0
yellow = 0
purple = 0
orange = 0

for i in range(9001):
    colorchoice = random.choice(colors)
    t1.color(colorchoice)
    t1.forward(400)
    t1.right(179)
    if colorchoice == "red":
        red += 1
    if colorchoice == "blue":
        blue += 1
    if colorchoice == "green":
        green += 1
    if colorchoice == "yellow":
        yellow += 1
    if colorchoice == "purple":
        purple += 1
    if colorchoice == "orange":
        orange += 1
    if red == 100 or blue == 100 or green == 100 or yellow == 100 or purple == 100 or orange == 100:
        print("Mexican Score: " + str(red) + "." + " Fry Night Score: " + str(blue) + "." + " Japaneese Score: " + str(green) + "." + " Make Score: " + str(yellow) + "." + " Johnathon's Score: " + str(purple) + "." + " BBQ Score: " + str(orange) + ".")
        break