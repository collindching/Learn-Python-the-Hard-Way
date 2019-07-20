## \ is a way to put difficult-to-type characters into a string (escape sequences)
    ## ie \\ or \' or \"

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

print('%r' % '\"') ## I feel like this should be outputting \"...
print('%r' % '\"\"')
print('%s' % '\"')
print('%s' % '\"\"')
print(r"\n")
