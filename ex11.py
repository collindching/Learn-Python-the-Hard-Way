print("How old are you?", end=' ')
age = input() ## raw_input() doesn't work in Python 3
print("How tall are  you", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print("So  you're %r old, %r tall and %r heavy." % (age, height, weight))

print("Where do you go to school?", end=' ')
school = input()
print("%s is a great school!" % school)