from sys import argv

script, input_file = argv

## prints contents of a file
def print_all(f):
    print(f.read())

## seek(0) moves the pointer of the filehandle to beginning of file
def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print(line_count,f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

## reset to beginning
rewind(current_file)

print("Let's print three lines:")

## each time you call readline, the filehandle moves down
current_line = 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

"""
How does readline() know where each line is?
Inside readline() is code that scans each byte of the file until it finds
a \n character, then stops reading to return. The file f maintains its current position
in the file after each readline() call... the current_file instance from open(input_file)"""