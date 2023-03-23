# File: Handicap.py
# Student: Nahee Kim
# UT EID: nk23395
# Course Name: CS303E
# 
# Date: Jan 28 2023
# Description of Program: This program will run calculations of an inputed bowler's average and handicap after 3 games.

#input for the bowler's name
name1 = input("Enter bowler's name: ")

#input for the bowler's first game score
score1 = int(input("Enter Game 1: "))

#input for the bowler's second game score
score2 = int(input("Enter Game 2: "))

#input for the bowler's third game score
score3 = int(input("Enter Game 3: "))

#adds space before the results
print()

#print the script for the handicap report
print("Handicap report for", name1)

#calculations for the bowler's average
average = (score1 + score2 + score3)/3
average = int(average)			#truncates positive floating point to int

#calculations for the bowler's handicap
handicap = (200 - average) * 0.80
handicap = int(handicap)			#truncates positive floating point to int
handicap = max(0, handicap)	#causes a negative handicap to be computed as zero

#enters the results of the computations
print("  Average is:", average)
print("  Handicap is:", handicap)

#print script for final line
print("It's time to Bowl!")
