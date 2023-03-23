# File: GuessingGame.py
# Student: Nahee Kim
# UT EID: nk23395
# Course Name: CS303E
# 
# Date: Feb 07 2023
# Description of Program: This is a program for a game where the goal is to guess a secret number in 10 tries. 

def main(initialAnswer = None):
	# gives GUESS a variable of 10 to set the limit of guesses
	GUESS = 10
	# import the "random" python
	import random
	# inputs empty space at top
	print()
	# intro to the game
	print("Welcome to the guessing game! Good luck!", "\n")
	# user can specify Y or N to play the game
	answer = input("Are you ready to play (Y/N):")
	print()
	if (answer == "N"):
		print("Well, come again later. Goodbye!", "\n")
	elif (answer == "Y"):
		print("See if you can guess the 'secret number'!", "\n")
		# if initalAnswer is specified and not NONE
		if initialAnswer:
      			thisGameAnswer = initialAnswer
		# otherwise, the 'secret number' is chosen at random within the range
		else:
      			thisGameAnswer = random.randint(1, 999)
		# imitates the loop for 10 guesses
		while(GUESS < 11):
			# counts down the number of guesses
			GUESS -= 1
			n = int(input("Enter an integer from 1 to 999: "))
			# considers the response to all possible input guesses
			if (n == thisGameAnswer):
				print("Congratulations, you got it! You took", 10 - GUESS, "guesses!", "\n")
				break
			elif (n < 1) or (n > 999):
				# function to not decrease the number of guesses
				GUESS += 1
				print("That's an illegal guess. Try again! You have", GUESS, "guesses left.", "\n")
			elif (n > thisGameAnswer):
				print("Your guess is too high. Try again! You have", GUESS, "guesses left.", "\n")
			elif (n < thisGameAnswer):
				print("Your guess is too low. Try again! You have", GUESS, "guesses left.", "\n")
			# function when you run out of guesses
			if (GUESS == 0):
				print("Sorry! You took too many guesses. The answer was ", thisGameAnswer, ". Better luck next time!", sep = "")
				# space at end
				print()
				# ends the loop
				break
	# response to user if neither Y or N was the input
	else:
		print("Sorry, I didn't recognize your answer. Try again!")
		#space at end
		print()
		return

main()
