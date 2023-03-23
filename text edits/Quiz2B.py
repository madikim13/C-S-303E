# CS 303E Quiz 2
# do NOT rename this file, otherwise Gradescope will not accept your submission


# Problem 1: Book Purchases
def bookPurchases():
    # write your solution to problem 1 here
    x = input()
    y = input()
    "Harry Potter" == 5.42
    "Percy Jackson" == 3.33
    "Hunger Games" == 2.10
    "Divergent" == 1.94
    "LotR" == 1.42
    total = 14.21 - x - y
    print("$", format(total, "0.2f"), sep="")
    pass


# Problem 2: First Term Larger Than k
def firstTermLarger():
    # write your solution to problem 2 here
    n = 1
    k = float(input())
    while True:
        n += 1
        a = 2.242 * (n ** 3) - (n ** 2)
        if (a > k):
            print(format(a, "0.2f"))
            break
    pass


if __name__=="__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.
    
    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """
    # bookPurchases()
    firstTermLarger()

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT
