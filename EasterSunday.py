# File: EasterSunday.py
# Student: Nahee Kim
# UT EID: nk23395
# Course Name: CS303E
# 
# Date: 1/22/23
# Description of Program: The program computes the date of Easter Sunday for any inputed year

# set variable y as the input year 
y = int(input("Enter year: "))

# set variable a as the remainder of y divided by 19
a = y % 19

# set variable b and c
b = y // 100		# b is the quotient of y divided by 100
c = y % 100		# c is the remainder of y divided by 100

# set variable d and e
d = b // 4		# d is the quotient of b divided by 4
e = b % 4		# e is the remainder of b divided by 4

# set variable g as the quotient of the function below
g = (8 * b + 13) // 25

# set variable h as the remainder of the function below
h = (19 * a + b - d - g +15) % 30

# set variable j and k
j = c // 4		# j is the quotient of c divided by 4
k = c % 4		# k is the remainder of c divided by 4

# set variable m as the quotient of the function below
m = (a + 11 * h) // 319

# set variable r as the remainder of the function below
r = (2 * e + 2 * j - k - h +m +32) % 7

# set variable n as the quotient of the function below
n = (h - m + r + 90) // 25

# set variable p as the remainder of the function below
p = (h - m + r + n + 19) % 32

# compute a script for the date of Easter Sunday for the inputed year
print("In", y, "Easter Sunday is on month", n, "and day", p)
