"""
While-Loops

1. Use while-loops sparingly
2. Make sure there is a stop in your while
3. Print out your test var at the top and bottom of the while-loop to check
"""

def addNumbers(x):
    i = 0
    numbers = []

    while i < 6:
        print("At the top i is %d" % i)
        numbers.append(i)

        i = i + 2
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

    for num in numbers:
        print(num)

addNumbers(6)