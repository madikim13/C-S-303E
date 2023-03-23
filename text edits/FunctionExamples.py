# File: FunctionExamples.py
# Student: Nahee Kim
# UT EID: nk23395
# Course Name: CS303E
# 
# Date Created: Feb 14 2023
# Description of Program: A program that runs 12 different functions

def sum3Numbers(x, y, z):
	# return the sum of the three parameters
	return x + y + z

def multiply3Numbers(x, y, z):
	# return the product of the three parameters
	return x * y * z

def sumUpTo3Numbers(x, y = 0, z = 0):
	# return the sum of up to three parameters
	return x + y + z

def multiplyUpTo3Numbers (x, y = 1, z = 1):
	# return the product of up to three parameters
	return x * y * z

def printInOrder(x, y):
	# takes 2 numbers as input and prints them out in ascending order
	if (x > y):
		print(x, y)
	elif (y > x):
		print(y, x)

def areaOfSquare(side):
	# return the area of a square, given the length of a side
	if (side >= 1):
		return side ** 2
	elif (side < 1):
		print("Illegal input. Length of a side must be positive.")

def perimeterOfSquare(side):
	# return the perimeter of a square, given the length of a side
	if (side >= 1):
		return 4 * side
	elif (side < 1):
		print("Illegal input. Length of a side must be positive.")

def areaOfCircle(radius):
	# return the area of a circle, given the radius
	import math
	if (radius >= 1):
		return (radius ** 2) * math.pi
	elif (radius < 1):
		print("Illegal input. Radius must be positive.")

def circumferenceOfCircle(radius):
	# return the circumference of a circle, given the radius
	import math
	if (radius >= 1):
		return (2 * radius) * math.pi
	elif (radius < 1):
		print("Illegal input. Radius must be positive.")

def bothFactors(d1, d2, x):
	# return whether both d1 and d2 are both factors (evenly divide) x, given 3 parameters d1, d2, x
	if (x % d1 == 0) and (x % d2 == 0):
		return True
	else:
		return False

def squareAndCircle(x):
	# compute and print out the area and circumference of a circle with radius x and the area and perimeter of a square with side x
	print()
	print("Circle with radius", x, "has:")
	circleArea = areaOfCircle(x)
	print("	Area:", circleArea)
	circleCircumference = circumferenceOfCircle(x)
	print("	Circumference:", circleCircumference)
	print("Square with side", x, "has:")
	squareArea = areaOfSquare(x)
	print("	Area:", squareArea)
	squarePerimeter = perimeterOfSquare(x)
	print("	Perimeter:", squarePerimeter)
	print()

def factorial(n):
	# return the factorial of n
	prod = 1
	if (n < 1):
		print("Illegal input. Inputed number must be positive.")
	else:
		for i in range (1, n + 1):
			prod *= i
		return prod
			
		
