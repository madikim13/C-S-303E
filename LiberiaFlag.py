# File: LiberiaFlag.py
# Student: Nahee Kim
# UT EID: nk23395
# Course Name: CS303E
# 
# Date: APR 11 2023
# Description of Program: This program draws the Liberia flag using Turtle graphics commands.

import turtle

def drawSquare(ttl, x, y):
	ttl.penup()
	ttl.goto(x, y)
	ttl.setheading(0)
	ttl.pendown()
	ttl.pencolor("Blue")
	ttl.fillcolor("Blue")
	ttl.begin_fill()
	for count in range(4):
		ttl.forward(98)
		ttl.right(90)
	ttl.end_fill()
	ttl.penup()

def drawRedRectangle(ttl, x, y):
	ttl.penup()
	ttl.goto(x, y)
	ttl.pencolor("Red")
	ttl.fillcolor("Red")
	for stripes in range(y, 110, 40):
		ttl.goto(x, stripes)
		ttl.pendown()
		ttl.setheading(0)
		ttl.begin_fill()
		for count in range(20):
			ttl.forward(418)
			ttl.goto(x, stripes + count)
		ttl.end_fill()
		ttl.penup()

def drawWhiteRectangle(ttl, x, y):
	ttl.penup()
	ttl.goto(x, y)
	ttl.pencolor("White")
	ttl.fillcolor("White")
	for stripes in range(y, 110, 40):
		ttl.goto(x, stripes)
		ttl.pendown()
		ttl.setheading(0)
		ttl.begin_fill()
		for count in range(20):
			ttl.forward(418)
			ttl.goto(x, stripes + count)
		ttl.end_fill()
		ttl.penup()

def drawStar(ttl, x, y):
	ttl.penup()
	ttl.goto(x, y)
	ttl.pendown()
	ttl.pencolor("White")
	ttl.fillcolor("White")
	ttl.begin_fill()
	ttl.forward(15)
	for segments in range(9):
		if segments % 2 == 0:
			ttl.left(72)
			ttl.forward(25)
		else:
			ttl.right(144)
			ttl.forward(25)
	ttl.end_fill()
	ttl.penup()

def drawOutline(ttl, x, y):
	ttl.penup()
	ttl.pendown()
	ttl.setheading(0)
	ttl.pencolor("Black")
	ttl.goto(x, y)
	ttl.forward(418)
	ttl.right(90)
	ttl.forward(220)
	ttl.right(90)
	ttl.forward(418)
	ttl.right(90)
	ttl.forward(220)
	ttl.penup()

Monty = turtle.Turtle()
Monty.speed(50)
drawRedRectangle(Monty, -209, -110)
drawWhiteRectangle(Monty, -209, -90)
drawSquare(Monty, -209, 108)
drawStar(Monty, -183.5, 70)
drawOutline(Monty, -209, 110)

turtle.done()