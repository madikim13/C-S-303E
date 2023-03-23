# File: FindPrimeFactors.py
# Student: Nahee Kim
# UT EID: nk23395
# Course Name: CS303E
# 
# Date: Mar 10 2023
# Description of Program: The program takes a prime number input and returns a list of its prime factors.

factors = []

def main():
	print("Find Prime Factors:")
	while True:
		x = int(input("Enter a positive integer (or 0 to stop): "))
		if x == 0:
			print("Goodbye!")
			print()
			break
		elif x < 0:
			print("Negative integer entered. Try again.")
			print()
		elif x == 1:
			print("1 has no prime factorization.")
			print()
		else:
			findPrimeFactors(x)
			print("The prime factorization of", x, "is:", factors)
			factors.clear()
			print()

def findNextPrime(num):
	if (num < 2):
		return 2
	elif (num % 2 == 0):
		num -= 1
	guess = num + 2
	while (not isPrime(guess)):
		guess += 2
	return guess

def findPrimeFactors(num):
	d = 1
	while True:
		if isPrime(num):
			factors.append(num)
			break
		elif (num % findNextPrime(d) == 0):
			num = num // findNextPrime(d)
			factors.append(findNextPrime(d))
			if isPrime(num):
				factors.append(num)
				break
			else:
				continue
		else:
			d += 1

def isPrime(num):
	import math
	if (num <2 or num % 2 == 0):
		return (num == 2)
	divisor = 3
	while (divisor <= math.sqrt(num)):
		if (num % divisor == 0):
			return False
		else:
			divisor += 2
	return True

main()
			

	