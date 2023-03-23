# File: Project1.py
# Student: Nahee Kim
# UT EID: nk23395
# Course Name: CS303E
# 
# Date: Feb 24 2023
# Description of Program: Program runs a game of rock, paper, and scissors, one gives statistics of the games as well.

ROCK = "1"
PAPER = "2"
SCISSORS = "3"

print("Welcome to a game of Rock, Paper, Scissors!")

def machinePlay():
	# program chooses one of the three moves randomly
	import random
	play = random.choice([ROCK, PAPER, SCISSORS])
	return play

def playName(play):
	# returns the play names to lowercase versions
	if play == ROCK:
		return "rock"
	elif play == PAPER:
		return "paper"
	elif play == SCISSORS:
		return "scissors"

def main():
	# the main game will be played in this function
	plays = 0
	wins = 0
	losses = 0
	draws = 0
	while True:
		plays += 1
		print()
		print("Choose your play:" + "\n" +
			"  Enter 1 for rock;" + "\n" +
			"  Enter 2 for paper;" + "\n" +
			"  Enter 3 for scissors;")
		play1 = input("  Enter 4 to exit: ")
		play2 = machinePlay()
		if (play1 == "4"):
			plays -= 1
			if (plays == 0):
				print("No games were completed." + "\n" +
					"Thanks for playing. Goodbye!")
				break
			else:
				return printStats(plays, wins, losses, draws)
		elif (play1 == ROCK) or (play1 == PAPER) or (play1 == SCISSORS):
			if (play1 == play2):
				print("You played ", playName(play1), "; ", "your opponent played ", playName(play2) + "\n" + "There's no winner. Try again!", sep="")
				draws += 1
			elif (play1 == ROCK and play2 == PAPER) or (play1 == PAPER and play2 == SCISSORS) or (play1 == SCISSORS and play2 == ROCK):
				print("You played ", playName(play1), "; ", "your opponent played ", playName(play2) + "\n" + "Sorry, you lost!", sep="")
				losses += 1
			elif (play1 == ROCK and play2 == SCISSORS) or (play1 == PAPER and play2 == ROCK) or (play1 == SCISSORS and play2 == PAPER):
				print("You played ", playName(play1), "; ", "your opponent played ", playName(play2) + "\n" + "Congratulations, you won!", sep="")
				wins += 1
		else:
                        plays -= 1
                        print("Illegal play entered. Try again!")

def printStats(plays, wins, losses, draws):
	# prints the statistics of the game based on the outcomes
	youWon = wins/plays
	youLost = losses/plays
	noWinner = draws/plays
	print("Game statistics:")
	print(format("  Games played:", ">3s"), plays)
	print("  You won: ", format(wins, "5.0f"), "(" + format(youWon, "0.1%") + ")", "\n" + \
		"  You lost: ", format(losses, "4.0f"), "(" + format(youLost, "0.1%") + ")", "\n" + \
		"  No winner: ", format(draws, "3.0f"), "(" + format(noWinner, "0.1%") + ")")
	print("Thanks for playing. Goodbye!")
	
main()
