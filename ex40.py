mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

"""
A module is a Python file with functions or variables in it

You then import that file

You can access the functions or variables in that module with the '.' (dot) operator
"""

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()