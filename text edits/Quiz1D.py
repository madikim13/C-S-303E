# CS 303E Quiz 1D
# do NOT rename this file, otherwise Gradescope will not accept your submission


# Problem 1: Gossip Gains
def gossipGains():
    # write your solution to problem 1 here
    import math
    F = float(input())  
    W = float(input())  
    H = float(input())  
    Revenue = math.sqrt((F ** 3) / 4) + 12.5 * ((W ** 2) / H)
    float(Revenue)
    print("You will gain $", format(Revenue, '.2f'), sep="")
    pass


# Problem 2: Cookie Baking
def cookieBaking():
    # write your solution to problem 2 here
    E = int(input())  
    S = float(input())  
    F = float(input())
    batch1 = (E // 4)
    batch2 = (S // 3.3)
    batch3 = (F // 5.9)
    int(batch1)
    int(batch2)
    int(batch3)
    print(format((min(batch1, batch2, batch3)), '.0f'))
    pass


if __name__=="__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.
    
    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """
    gossipGains()
    cookieBaking()

    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT
