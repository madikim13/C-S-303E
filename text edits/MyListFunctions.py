# File: MyListFunctions.py
# Student: Nahee Kim
# UT EID: nk23395
# Course Name: CS303E
# 
# Date: Mar 21 2023
# Description of Program: This program is a collection of functions to manipulate lists

def myAppend(lst, x):
	# Return a new list that is like lst but with 
	# the element x at the right end
	return lst + [x]

def myExtend(lst1, lst2):
	# Return a new list that contains the elements of
	# lst1 followed by the elements of lst2 in order.
	return lst1 + lst2

def myMax(lst):
	# Return the element with the highest value.
	if len(lst) == 0:
		print("Empty list: no max value")
		return
	else:
                return max(lst)

def mySum(lst):
	# Return the sum of the elements in lst.
	sum = 0
	for i in range(len(lst)):
		sum += lst[i]
	return sum

def myCount(lst, x):
	# Return the number of times element x appears
	# in lst.
	found = []
	for i in range (len(lst)):
		if x == lst[i]:
			found += [i]
	return len(found)

def myInsert(lst, i, x):
	# Return a new list like lst except that x has been
	# inserted at the ith position.
        found = []
        found2 = []
        if (i < 0) or (i > len(lst)):
                print("Invalid Index")
        else:
                for y in range(i):
                        found.append(lst[y])
                for y in range(i, len(lst)):
                        found2.append(lst[y])
                return found + [x] + found2
                
                
def myPop(lst, i):
	# Return two results: 
	# 1. a new list that is like lst but with the ith 
	#    element removed;
	# 2. the value that was removed.
        found = []
        if (i < 0) or (i >= len(lst)):
                print("Invalid index")
                return lst, None
        else:
                return list(x for x in lst if x != lst[i]), lst[i]

def myFind(lst, x):
	# Return the index of the first (leftmost) occurrence of 
	# x in lst, if any.
	for i in range(len(lst)):
		if x == lst[i]:
			return i
	return -1

def myRFind(lst, x):
	# Return the index of the last (rightmost) occurrence of 
	# x in lst, if any. Return -1 if ch does not occur in lst.
	for i in range((len(lst)-1), 0, -1):
		if x == lst[i]:
			return i
	return -1

def myFindAll(lst, x):
	# Return a list of indices of occurrences of x in lst, if any.
	# Return the empty list if there are none.
	found = []
	for i in range(len(lst)):
		if x == lst[i]:
			found += [i]
	return found
	
def myReverse(lst):
	# Return a new list like lst but with the characters
	# in the reverse order.
	found = []
	for i in range(len(lst)):
		x = lst[-(i + 1)]
		found += [x]
	return found

def myRemove(lst, x):
	# Return a new list with the first occurrence of x
	# removed.  If there is none, return lst.
        found = []
        found2 = []
        if x in lst:
                for i in range(len(lst)):
                        if x == lst[i]:
                                for y in range(i):
                                        found.append(lst[y])
                                for y in range(i+1, len(lst)):
                                         found2.append(lst[y])
                                return found + found2
        else:
                return lst

def myRemoveAll(lst, x):
	# Return a new list with all occurrences of x
	# removed.  If there are none, return lst.
        found = []
        for i in range (len(lst)):
                if x == lst[i]:
                        found += [i]
        if len(found) == 0:
                return lst
        else:
                print(list(i for i in lst if i != x))
		
def mySlice(lst, i, j):
	# A limited version of the slice operations on lists.
	# If i and j are in [0..len(lst)], return the list 
	# [ lst[i], lst[i+1], ... lst[j-1] ].  I.e., 
	# the slice lst[i:j].  Print an error message if either
	# i or j is not in [0..len(lst)].  Notice that this is 
	# similar but not identical to the way Python slice behaves.
        found = []
        if (0 <= i <= len(lst)) and (0 <= j <= len(lst)):
                while i < j:
                        i += 1
                        found.append(lst[i-1])
                return found
        else:
                print("Illegal index value")
