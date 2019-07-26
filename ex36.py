"""
Designing and debugging

Rules for if-statements
1. Every if-statement must have an else
2. Try to always have an else statement
3. Don't nest if-statements more than two deep
4. Treat if-statements like paragraph
5. Your boolean tests should be simple

Rules for loops
1. Use a while-loop only to loop forever
2. Use a for-loop for all other kinds of looping

Tips for debugging
1. Do not use a debugger
2. Best way to debug a program is to use print
3. Make sure parts of your programs work as you work on them...
don't write massive files of code before you try to run them
"""


def tree():
    print("You climb 10 feet and see an angry woodpecker. What do you do?")

    next = input('> ')

    if "fight" in next:
        end("You fight and kill it.")
    elif any(word in next for word in ['run','escape','flee','jump']):
        end("You fall off the tree and die.")
    else:
        print("Didn't recognize statement!")

def hole():
    print("You burrow into the gopher hole. It's nice and warm. Do you want to sleep here?")

    next = input('> ')

    if "yes" in next:
        end("Win.")
    elif "no" in next:
        end("Lose.")
    else:
        print("Didn't recognize statement.")


def end(outcome):
    print(outcome,"Good job!")

def start():
    print("You're in a forest.")
    print("There are trees all around you and a hole in the ground.")
    print("What do you do?")

''
    next = input('> ')

    if "climb up" in next:
        tree()
    elif "hole" in next:
        hole()
    else:
        print("end")

start()

