## Strings and Text

## f-string with 10 plugged in
x = f"There are {10} types of people."
binary = "binary"
do_not = "don't"
## f-string with binary and do_not variables plugged in; two strings within a string
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

## both f-strings, with string inside a string
print(f"I said: {x}.")
print(f"I also said: {y}.")

hilarious = False
joke_evaluation = f"Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print(w+e)
## adding two string w and e means string concatenation