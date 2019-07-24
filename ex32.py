"""
Loops and Lists
"""

## examples of lists
hairs = ['brown','blond','red']
eyes = ['brown','blue','green']
weights = [1,2,3,4]

the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print("This is count %d" % number)

for fruit in fruits:
    print("A fruit of type: %s" % fruit)

for i in change:
    print("I got %r" % i)

elements = []

for i in range(0, 6):
    print("Adding %d to the list." % i)
    elements.append(i)

## You can also do this, which converts a range object to a list object
elements = list(range(0,6))

for i in elements:
    print("Element was: %d" % i)
