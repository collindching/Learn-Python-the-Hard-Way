formatter = "%r %r %r %r"

print(formatter % (1,2,3,4))
print(formatter % ('one','two','three','four'))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
## Python prints strings as efficiently as possible when you use %r, which is why one of these is in single quotes
print(formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))