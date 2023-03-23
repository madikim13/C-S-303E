# File: Student.py
# Student: Nahee Kim
# UT EID: nk23395
# Course Name: CS303E
# 
# Date: Feb 21 2023
# Description of Program: This program defines a simple class with a given student and their exam grades.

class Student:
        # sets a class for the attributes and methods
        def __init__(self, name = None, Exam1 = None, Exam2 = None):
                self.__name = name
                self.__Exam1 = Exam1
                self.__Exam2 = Exam2

        # prints a set of strings with the name and grades for exams
        def __str__(self):
                return "Student: " + str(self.__name) + "\n" + \
                       format("Exam1: ", ">9s") + str(self.__Exam1) + "\n" + \
                       format("Exam2: ", ">9s") + str(self.__Exam2)

        # prints the inputed name
        def getName(self):
                return self.__name

        # setter: sets an inputed grade as Exam 1
        def setExam1Grade(self, Exam1):
                self.__Exam1 = Exam1

        # setter: sets an inputed grade as Exam 2
        def setExam2Grade(self, Exam2):
                self.__Exam2 = Exam2
                
        # getter: prints set grade of Exam 1
        def getExam1Grade(self):
                return self.__Exam1

        # getter: prints set grade of Exam 2
        def getExam2Grade(self):
                return self.__Exam2

        # calculates the average of the exams 
        def getAverage(self):
                if (self.__Exam1 == None) or (self.__Exam2 == None):
                        # prints error message if exam grade is not specified
                        print("Some exam grades not available.")
                else:
                        return (int(self.__Exam1) + int(self.__Exam2)) / 2


