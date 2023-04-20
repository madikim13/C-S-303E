# CS 303E Quiz 5B
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters


# Problem 1: First Uppercase Locations
def firstUppercaseLocations(strings):
    capital = {}
    for key in strings:
        for i in range(len(key)):
            if key.islower():
                capital[key] = -1
            else:
                if key[i].isupper():
                    capital[key] = i
                else:
                    continue
    return capital
    pass



# Problem 2: List of Big Integers
def bigIntegers(nums):
    if nums == []:
        return []
    else:
        if abs(int(nums[0])) > 20:
            return [nums[0]] + bigIntegers(nums[1:])
        else:
            return bigIntegers(nums[1:])
    pass



if __name__ == '__main__':
    # uncomment the following lines to run the given test cases
    # note that the output will look slightly different
    # due to how the expected output is formatted

    # print(firstUppercaseLocations({"heLlo", "world"}))
    # print(firstUppercaseLocations({"Hi", "welCOme", "to", "Chili's!"}))
    # print(firstUppercaseLocations({"that'S", "all", "I", "got!"}))

    # print(bigIntegers([38, 5, 10, -11, 20, 49, -19, 38, -11, 29, 0, -28]))
    # print(bigIntegers([20, 90, 83]))
    # print(bigIntegers([10, 13]))

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT
