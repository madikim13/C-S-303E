# File: Benford.py
# Student: Nahee Kim
# UT EID: nk23395
# Course Name: CS303E
# 
# Date: Mar 29 2023
# Description of Program: programs verifies Benford's law for U.S. census data from 2009, writing the file into benford.txt

import os.path

def main():
        f1 = input("Enter the name of a file of census data: ").strip()
        if not os.path.isfile(f1):
                print("File does not exist")
                return
        infile = open(f1, "r")
        outfile = open("benford.txt", "w")
        popCount = set()
        cityCount = []
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        count5 = 0
        count6 = 0
        count7 = 0
        count8 = 0
        count9 = 0
        dictDigit = {"1": count1, "2": count2, "3": count3, "4": count4, \
                     "5": count5, "6": count6, "7": count7, "8": count8, \
                     "9": count9}
        line = infile.readline()
        for line in infile:
                words = line.split()
                for count in words:
                        if count.isdigit() == True:
                                popCount.add(count)
                                cityCount.append(count)
        for i in cityCount:
                str(i)
                if int(str(i)[0]) == 1:
                        count1 += 1
                if int(str(i)[0]) == 2:
                        count2 += 1
                if int(str(i)[0]) == 3:
                        count3 += 1
                if int(str(i)[0]) == 4:
                        count4 += 1
                if int(str(i)[0]) == 5:
                        count5 += 1
                if int(str(i)[0]) == 6:
                        count6 += 1
                if int(str(i)[0]) == 7:
                        count7 += 1
                if int(str(i)[0]) == 8:
                        count8 += 1
                if int(str(i)[0]) == 9:
                        count9 += 1
                dictDigit["1"] = count1
                dictDigit["2"] = count2
                dictDigit["3"] = count3
                dictDigit["4"] = count4
                dictDigit["5"] = count5
                dictDigit["6"] = count6
                dictDigit["7"] = count7
                dictDigit["8"] = count8
                dictDigit["9"] = count9
        outfile.write("Total number fo cities: " + str(len(cityCount)))
        outfile.write("\n")
        outfile.write("Unique population counts: " + str(len(popCount)))
        outfile.write("\n")
        outfile.write("First digit frequency distributions:")
        outfile.write("\n")
        outfile.write("Digits  " + "Count   " + "Percentage")
        outfile.write("\n")
        for key in dictDigit:
                x = float((dictDigit[key]) / len(cityCount)) * 100
                outfile.write(format(key, "<8s") + format(dictDigit[key], "<8d") + \
                              format(x, "<.1f"))
                outfile.write("\n")
        infile.close()
        outfile.close()
        print("Output written to benford.txt")

main()
