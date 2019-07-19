## String formatting
## string formatting is for making strings that have variables embedded in them
## you embed variables inside a string by using specialized format sequences and putting varriables at the end

name = 'Zed A. Shaw'
age = 35
height = 74
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

print(f"If I add {age}, {height}, and {weight}, I get {age+height+weight}")