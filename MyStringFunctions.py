# File: MyStringFunctions.py
# Student: Nahee Kim
# UT EID: nk23395
# Course Name: CS303E
# 
# Date: Mar 4 2023
# Description of Program: This program runs a multitude of functions on strings.

def myAppend(s, ch):
	# Return a new string that is like s but with 
	# character ch added at the end
	return s + ch

def myCount(s, ch):
	# Return the number of times character ch appears
	# in s.
	return s.count(ch)

def myExtend(s1, s2):
	# Return a new string that contains the elements of
	# s1 followed by the elements of s2, in the same
	# order they appear in s2.
	return s1 + s2

def myMin(s = None):
	# Return the character in s with the lowest ASCII code.
	# If s is empty, print "Empty string: no min value"
	# and return None.
	if s == None:
		print("Empty string: no min value")
		return
	else:
		return min(s)

def myInsert(s, i, ch):
	# Return a new string like s except that ch has been
	# inserted at the ith position. I.e., the string is now
	# one character longer than before. Print "Invalid index" if
	# i is greater than the length of s and return None.
	if i > len(s):
		print("Invalid index")
	else:
		return s[ : i] + ch + s[i : ]

def myPop(s, i):
	# Return two results: 
	# 1. a new string that is like s but with the ith 
	#    element removed;
	# 2. the value that was removed.
	# Print "Invalid index" if i is greater than or 
	# equal to len(s), and return s unchanged and None
	if i >= len(s):
		print("Invalid index")
		return (s, "None")
	else:
		return (s[ : i] + s[i+1: ], s[i])
	

def myFind(s, ch):
	# Return the index of the first (leftmost) occurrence of 
	# ch in s, if any. Return -1 if ch does not occur in s.
	return s.find(ch)

def myRFind(s, ch):
	# Return the index of the last (rightmost) occurrence of 
	# ch in s, if any. Return -1 if ch does not occur in s.
	return s.rfind(ch)

def myRemove(s, ch):
	# Return a new string with the first occurrence of ch 
	# removed. If there is none, return s.
	if ch in s:
		index = s.find(ch)
		remove = s[:index] + s[index+1:]
		return remove
	else:
		return s

def myRemoveAll(s, ch):
	# Return a new string with all occurrences of ch.
	# removed. If there are none, return s.
	if ch in s:
		for i in range(myCount(s, ch) + 1):
			myRemove(s, ch)
			return s
	else:
		return s

def myReverse(s):
	# Return a new string like s but with the characters
	# in the reverse order.
	return s[len(s): : -1]
