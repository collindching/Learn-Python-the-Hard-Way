from sys import exit


class Engine:

    def __init__(self, map):
        self.map = map

        print("Welcome to HS Baller Simulator!")
        print("You're a high school freshman who's trying to make the varsity basketball team.")
        print("Develop your skills and try out for a place on the team when you're ready.")
        print("Good luck and remember: ball is life.")
        print()

    def play(self):
        next_scene = self.map.get_scene('bedroom')

        while True:
            curr_scene = next_scene
            next_scene = self.map.get_scene(curr_scene)


class Scene:

    # plays the scene out, returns a string corresponding to next scene
    def enter(self):
        pass


class Bedroom(Scene):

    def enter(self):
        print("Good morning from you bedroom! Where do you want to go?")
        print("(1) Go to the park")
        print("(2) Go to the gym")
        print("(3) Go to basketball tryouts")

        choice = int(input('> '))
        print()

        if choice == 1:
            return 'park'
        elif choice == 2:
            return 'gym'
        elif choice == 3:
            return 'tryouts'
        else:
            print("Choose 1, 2, or 3.")
            self.enter()


class Park(Scene):

    def __init__(self, player):
        self.player = player

    def enter(self):
        print("It's a sunny day at the park.")
        print("You can (1) play pickup, (2) go for a walk, or (3) relax.")
        print("What do you want to do?")

        choice = int(input('> '))

        if choice == 1:
            print("You played several solid games of pickup.")
            self.player.increase_strength(1)
            self.player.increase_endurance(1)
            self.player.increase_skill(1)

        elif choice == 2:
            print("While walking, you ponder some new basketball strategies.")
            self.player.increase_skill(2)

        elif choice == 3:
            print("You take some time for much-needed relaxation.")
            self.player.increase_endurance(1)

        else:
            print("Choose 1, 2, or 3.")

        self.player.print_stats()

        print("It's getting dark outside and you're tired from the day.")
        input("Press enter to head home. ")
        print()

        return('sleep')

class Gym(Scene):

    def __init__(self, player):
        self.player = player

    def enter(self):
        print("Ah, back at the iron temple.")
        print("You can (1) do cardio, (2) lift weights, or (3) shoot around.")
        print("What do you want to do?")

        choice = int(input("> "))

        if choice == 1:
            print("You do sprints at the treadmills, followed by stairmaster.")
            self.player.increase_endurance(3)

        elif choice == 2:
            print("You get a good pump in.")
            self.player.increase_strength(3)

        elif choice == 3:
            print("You put up some shots.")
            self.player.increase_skill(3)

        else:
            print("Choose 1, 2, or 3.")
            self.enter()

        self.player.print_stats()

        print("You've got a solid workout in and are ready to rest.")
        input("Press enter to head home. ")
        print()

        return('sleep')


class Tryouts(Scene):

    def __init__(self, player):
        self.player = player

    def enter(self):
        print("You're a little nervous but you've been practicing for a long time.")
        print("You're ready to do this.")

        if self.player.sum_stats() > 30:
            return 'finished'
        else:
            print("You played your hardest, but didn't quite play your best.")
            print("Luckily, there's another round of tryouts coming up.")
            print("Keep training and you'll get there soon.")
            input("Press enter to head home. ")
            print()

            return 'sleep'


class Sleep(Scene):

    def enter(self):
        print("You're back home, tucked into bed.")
        print("Good night. Today is a new day, a new opportunity!")
        input("Press enter to start the next day. ")
        print()

        return 'bedroom'


class End(Scene):

    def enter(self):
        print("You finish try outs and feel pretty good.")
        print("The head coach pulls you aside and commends you on your performance.")
        print("He doesn't usually do this, but he offers you a spot on the time")
        print("then and there. Congrats!")
        print("Your hard work paid off.")
        input("Hit enter to end the game. ")
        print()
        exit()

class Player:

    def __init__(self, name, strength, endurance, skill):
        self.name = name
        self.strength = strength
        self.endurance = endurance
        self.skill = skill

    def __str__(self):
        return f"My name is {self.name}.\nStrength: {self.strength}\nEndurance: {self.endurance}\nSkill: {self.skill}"

    def get_name(self):
        return self.name

    def get_strength(self):
        return f"Your strength is {self.strength}"

    def get_endurance(self):
        return f"Your endurance is {self.endurance}"

    def get_skill(self):
        return f"Your skill is {self.skill}"

    def increase_strength(self, n):
        self.strength += n
        return None

    def increase_endurance(self, n):
        self.endurance += n
        return None

    def increase_skill(self, n):
        self.skill += n
        return None

    def print_stats(self):
        print(self.get_strength(), self.get_endurance(), self.get_skill(), sep='\n')
        print()
        return None

    def sum_stats(self):
        return self.strength + self.endurance + self.skill

class Map:
    scenes = {
        'bedroom': Bedroom,
        'park': Park,
        'gym': Gym,
        'tryouts': Tryouts,
        'sleep': Sleep,
        'finished': End
    }

    def __init__(self, player):
        self.player = player

    def get_scene(self, scene_name):
        if scene_name in ['park', 'gym', 'tryouts']:
            return self.scenes[scene_name](self.player).enter()
        else:
            return self.scenes[scene_name]().enter()


def main():
    print("What's your player's name?")
    name = input("> ")

    print("Are you playing on easy, medium, or hard?")
    difficulty = input("> ")
    print("\nOkay!")

    if difficulty == "easy":
        player = Player(name, 8, 8, 8)
        player.print_stats()
    elif difficulty == "medium:":
        player = Player(name, 5, 5, 5)
        player.print_stats()
    elif difficulty == "hard":
        player = Player(name, 3, 3, 3)
        player.print_stats()
    else:
        print("Sorry, that wasn't a valid option.")
        return main()

    game_map = Map(player)
    game = Engine(game_map)
    game.play()

main()
