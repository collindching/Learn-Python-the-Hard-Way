## close closes file
## read reads contents of file
## readline rads one line of file
## truncate empties file
## write(stuff) writes stuff to file

from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write("%s\n%s\n%s\n" % (line1,line2,line3))

print("And finally, we close it.")
target.close()