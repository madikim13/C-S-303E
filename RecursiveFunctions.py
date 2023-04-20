# File: RecursiveFunctions.py
# Student: Nahee Kim
# UT EID: nk23395
# Course Name: CS303E
# 
# Date: APR 4 2023
# Description of Program: This program runs a multitude of recursive functions.

def sumItemsInList(L):
	# Given a list of numbers, return the sum.
	if L == []:
		return 0
	else:
		return L[0] + sumItemsInList( L[1:] )

def countOccurrencesInList(key, L):
	# Return the number of times key occurs in list L.
	if not L:
		return 0
	elif key == L[0]:
                return 1 + countOccurrencesInList( key, L[1:] )
	else:
		return countOccurrencesInList( key, L[1:] )

def addToN (n):
	# Return the sum of the non-negative integers to n.
	if n == 0:
		return 0
	else:
		return n + addToN(n - 1)

def findSumOfDigits( n ):
	# Return the sum of the digits in a non-negative integer.
	lst = []
	if n == 0:
		return 0
	else:
		return (n % 10) + findSumOfDigits(n // 10)

def integerToBinary( n ):
	# Given a nonnegative integer n, return the
	# binary representation as a string.
	if n == 0:
		return 0
	elif n == 1:
                return 1
	else:
		return str(integerToBinary(n // 2)) + str(n % 2)
	

def integerToList( n ):
	# Given a nonnegative integer, return a list of the 
	# digits (as strings).
        if n == 0:
                return ["0"]
        elif n // 10 == 0:
                return [n]
        else:
                return integerToList(n // 10) + [str(n % 10)]

def isPalindrome( s ):
	# Return True if string s is a palindrome and False
	# otherwise. Count the empty string as a palindrome.
	if s == "" or len(s) == 1:
		return True
	elif s[0] != s[len(s) - 1]:
		return False
	else:
		return isPalindrome(s[1:len(s) - 1])

def findFirstUppercase( s ):
	# Return the first uppercase letter in 
	# string s, if any. Return None if there
	# is none.
	if s == "":
		return None
	elif 65 <= ord(s[0]) <= 90:
		return s[0]
	else:
		return findFirstUppercase(s[1::])

def findLastUppercase( s ):
	# Return the last uppercase letter in
	# string s, if any. Return None if there
	# is none.
	if s == "":
		return None
	elif 65 <= ord(s[len(s) - 1]) <= 90:
		return s[len(s) - 1]
	else:
		return findFirstUppercase(s[::-1])

def findFirstUppercaseIndexHelper( s, index ):
	# Helper function for findFirstUppercaseIndex.
	# Return the index of the first uppercase letter;
	# assume you are starting at index. Return -1 
	# if there is none.
        s.replace(" ", "")
        if s == "" or index == len(s):
                return -1
        elif index > len(s):
                if findFirstUppercaseIndexHelper(s, 0) == -1:
                        return -1
                else:
                        return index + findFirstUppercaseIndexHelper(s, 0)
        elif 65 <= ord(s[index]) <= 90:
                return index
        else:
                return findFirstUppercaseIndexHelper(s, index + 1)

def findFirstUppercaseIndex( s ):
	# Return the index of the first uppercase letter in 
	# string s, if any. Return -1 if there is none. This one
	# requires a helper function, which is the recursive
	# function.
	return findFirstUppercaseIndexHelper( s, 0 )
