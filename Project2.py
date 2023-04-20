# File: Project2.py
# Student: Nahee Kim
# UT EID: nk23395
# Course Name: CS303E
# 
# Date: Mar 24 2023
# Description of Program: This program simulates driving a toy car around a grid.

import random

EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270

def dirName(d):
# returns direction names to lowercase versions
	if d == 0 or d == EAST:
		return "East"
	elif d == 90 or d == NORTH:
		return "North"
	elif d == 180 or d == WEST:
		return "West"
	elif d == 270 or d == SOUTH:
		return "South"

class ToyCar:

	def __init__(self, x = 0, y = 0, d = 0):
	# initializer for the class
		if (d > 270):
			print("ERROR: Illegal direction entered.")
		else:
			self.__x = x
			self.__y = y
			self.__d = d
	
	def __str__(self):
	# Generate a string containing information on 
	# the class object
		return "Your car is at location (" + str(self.__x) + ", " + str(self.__y) + \
		"), heading " + dirName(self.__d)

	def setDir(self, n):
	# validates the parameter and sets the direction accordingly
                self.__d = n
                print("DEBUG: setting direction", dirName(n))

	def getDir(self):
	# returns one of the directions:
	# 0, 90, 180, 270 (east, north, west, south)
		return self.__d

	def getX(self):
	# return the X coordinate of the car's location
                return self.__x

	def getY(self):
	# return the Y coordinate of the car's location
                return self.__y

	def turnLeft(self):
	# change direction 90 degrees to the left
		if self.__d == 270:
			self.__d -= 270
			print("DEBUG: turning", dirName(self.__d))
		else:	
			self.__d += 90
			print("DEBUG: turning", dirName(self.__d))

	def turnRight(self):
        # change direction 90 degrees to the right
		if self.__d == 0:
			self.__d += 270
			print("DEBUG: turning", dirName(self.__d))
		else:
			self.__d -= 90
			print("DEBUG: turning", dirName(self.__d))

	def forward(self, n):
	# move the car in the current direction
                if n < 0:
                        print("ERROR: Illegal distance entered.")
                else:
                        if self.__d == 0:
                                self.__x = int(self.__x) + n
                        elif self.__d == 90:
                                self.__y = int(self.__y) + n
                        elif self.__d == 180:
                                self.__x = int(self.__x) - n
                        elif self.__d == 270:
                                self.__y = int(self.__y) - n
                        print("DEBUG: moving forward", n)

def randomDrive(car, n):
	# drives the car randomly for n "moves"
	if n < 0:
		print("ERROR: Illegal value entered.")
	else:
		for i in range(n):
			i += 1
			move = random.randint(0, 100)
			turn = random.randint(1, 3)
			if turn == 1:
				car.turnRight()
			elif turn == 2:
				car.turnLeft()
			else:
				print("DEBUG: turning", dirName(car.getDir()))
			car.forward(move)
                
def goto(car, x, y):
	# drives the car to the specified coordinates (x, y)
	newX = abs(int(car.getX()) - x)
	newY = abs(int(car.getY()) - y)
	if x < 0 and y < 0:
		car.setDir(WEST)
		car.forward(newX)
		car.setDir(SOUTH)
		car.forward(newY)
	elif x < 0 and y > 0:
		car.setDir(WEST)
		car.forward(newX)
		car.setDir(NORTH)
		car.forward(newY)
	elif x > 0 and y < 0:
		car.setDir(EAST)
		car.forward(newX)
		car.setDir(SOUTH)
		car.forward(newY)
	elif x > 0 and y > 0:
		car.setDir(EAST)
		car.forward(newX)
		car.setDir(NORTH)
		car.forward(newY)

def gasStation():
	# generates random coordinates (x, y) in range [-100, 100]
	# where the gas station is located
	gasStation.gasX = random.randrange(-100,100)
	gasStation.gasY = random.randrange(-100,100)
	print("Located gas station at (", gasStation.gasX, ", ", gasStation.gasY, ")", sep = "")
	print("(", gasStation.gasX, ", ", gasStation.gasY, ")", sep = "")

def gasUp(car):
	# find the current location of the gas station and go there
	gasStation()
	return goto(car, gasStation.gasX, gasStation.gasY)
	
