# File: Project3.py
# Student: Nahee Kim
# UT EID: nk23395
# Course Name: CS303E
# 
# Date Created: APR 15 2023
# Date Last Modified: APR 16 2023
# Description of Program: The program reads the populations of most populous 500 Texas cities and returns a specific response based on the command users input.

import os
if not os.path.isfile("citiesData.csv"):
	print("File does not exist")
	exit()

print()
print("Welcome to the Texas Cities Population Dashboard.\n", \
"This provides census data from the 2020 census and\n", \
"estimated population data in Texas as of 2023.", sep="")
print()
print("Creating dictionary from file: citiesData.csv")

dict = {}
cities = []
pop2020 = 0
pop2023 = 0

def intro():
	print("Enter any of the following commands:\n", \
	"Help - list available commands;\n", \
	"Quit - exit this dashboard;\n", \
	"Cities - list all Texas cities;\n", \
	"Census <cityName>/Texas - population in 2020 census by specified city or statewide;\n", \
	"Estimated <cityName>/Texas - estimated population in 2023 by specified city or statewide;\n", \
	"Growth <cityName>/Texas - percent change from 2020 to 2023, by city or statewide.", sep="")

def file():
	infile = open("citiesData.csv", "r")
	line = infile.readline()
	while line:
		if line[0] == "#":
			line = infile.readline()
			continue
		else:
			data = line.split(",")
			z = data[3].strip('\"')
			x = int(data[0])
			y = int(data[1])
			global pop2020
			global pop2023
			pop2020 += y
			pop2023 += x
			cities.append(z)
			dict[z] = ((x, y))
		cities.sort()
		line = infile.readline()
	infile.close()

def main():
	while True:
		print()
		commandInput = input("Please enter a command: ")
		commWords = commandInput.split()
		comm = commWords[0].lower()
		args = commWords[1:]
		arg = " ".join(args)
		if comm == "help":
			intro()
		elif comm == "quit":
			print("Thank you for using the Texas Cities Population Database Dashboard. Goodbye!")
			print()
			break
		elif comm == "cities":
			for i in range(0, len(cities), 10):
				for j in range(10):
					print(cities[i + j], end = ", ")
				print()
		elif comm == "census":
			if arg == "Texas":
				print(arg, "'s ", "total population in the 2020 Census: ", pop2020, sep="")
			elif arg in cities:
				print(arg, "'s ", "total population in the 2020 Census: ", dict[arg][1], sep="")
			else:
				print("City", args, "is not recognized.")
		elif comm == "estimated":
			if arg == "Texas":
				print(arg, "'s ", "estimated population in 2023: ", pop2023, sep="")
			elif arg in cities:
				print(arg, "'s ", "estimated population in 2023: ", dict[arg][0], sep="")
			else:
				print("City", args, "is not recognized.")
		elif comm == "growth":
			if arg == "Texas":
				print(args, "had percent population change 2020 to 2023:", format(((pop2023 - pop2020)/pop2020), "0.2%"))
			elif arg in cities:
				print(args, "had percent population change 2020 to 2023:", format(((dict[arg][0] - dict[arg][1])/dict[arg][1]), "0.2%"))
			else:
				print("City", args, "is not recognized.")
		else:
			print("Command is not recognized.  Try again!")
		
file()
intro()
main()
