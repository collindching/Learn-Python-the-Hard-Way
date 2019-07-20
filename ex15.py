## import argv from sys module
from sys import argv

## capture script name and file name from command line
script, filename = argv

## opens file
txt = open(filename)

## returns file's name, then reads the text within the file
print("Here's your file %r:" % filename)
print(txt.read())

## takes file name
print("Type the filename again:")
file_again = input("> ")

## opens file
txt_again = open(file_again)

## reads contents of file
print(txt_again.read())