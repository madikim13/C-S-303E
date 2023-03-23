# File: Zeller.py
# Student: Nahee Kim
# UT EID nk23395
# Course Name: CS303E
# 
# Date: Feb 03 2023
# Description of Program: A program that calculates the day of the week for any Gregorian calendar date.

def main():
	# takes the inputed year and converts it to an integer
	Y = int( input("\nEnter year (i.e. 2003): "))
	# prints error for years which are below 1753, thus cannot be computed
	if (Y < 1753):		
		print("Year must be > 1752. Illegal year entered:", Y, "\n")
		return
	# takes the inputed month and converts it to an integer
	m = int( input("Enter month (1-12): "))
	# prints error for months which are not in between 1-12, thus cannot be computed
	if (m < 1) or (m > 12):
		print("Month must be in between [1..12]. Illegal month entered:", m, "\n")
		return
	# accounts for month and year adjustment
	if (m == 1) or (m == 2):
		m = m + 12
		Y = Y - 1
	# takes the inputed day and converts it to an integer
	d = int( input("Enter day (1-31): "))
	# prints error for days which are not in between 1-31, thus cannot be computed
	if (d < 1) or (d > 31):
		print("Day must be in between [1..31]. Illegal day entered:", d, "\n")
		return
	# computes variable K from Y
	K = Y % 100
	# computes variable J from Y
	J = Y // 100
	# computes the day of the week, h, from all inputed variables 
	h = ( d + (13 * (m + 1))//5 + K + K//4 + J//4 + 5 * J) % 7
	# statements to encode h as the day of the weeks (0-6)
	if (h == 0):
		print("Day of the week is Sunday.")
	elif (h == 1): 
		print("Day of the week is Saturday.")
	elif (h == 2): 
		print("Day of the week is Monday.")
	elif (h == 3): 
		print("Day of the week is Tuesday.")
	elif (h == 4): 
		print("Day of the week is Wednesday.")
	elif (h == 5): 
		print("Day of the week is Thursday.")
	elif (h == 6): 
		print("Day of the week is Friday.")
	# leaves space at end
	print()

main()