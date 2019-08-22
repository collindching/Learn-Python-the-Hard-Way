class Scene:

    def enter(self):
        pass

class Bedroom(Scene):

    def enter(self):
        print("Good morning")


class Park(Scene):

    def enter(self):
        pass


class Gym(Scene):

    def enter(self):
        print("You can do cardio, lift weights, or shoot around. What do you want to do?")
        train = input("> ")

        if train == 'cardio':
            pass
        elif train == 'lift':
            pass
        elif train == 'shoot':
            pass
        else:
            print("Command not recognized.")

class Tryouts(Scene):
    pass

class Player:

    def __init__(self, name, strength, endurance, skill):
        self.name = name
        self.strength = strength
        self.endurance = endurance
        self.skill = skill
        self.energy = 10

    def increase_strength(self, n):
        self.strength += n

    def increase_endurance(self, n):
        self.endurance += n

    def increase_skill(self, n):
        self.skill += n

    def change_energy(self, n):
        self.energy -= n

    def print_strength(self):
        print(f"Your strength is {self.strength}")

    def print_endurance(self):
        print(f"Your endurance is {self.endurance}")

    def print_skill(self):
        print(f"Your skill is {self.endurance}")

    def print_energy(self):
        print(f"Your energy is {self.energy}")


class Map:

    def __init__(self, start_scene, name, difficulty):
        

        pass

    def next_scene(self, scene_name):
        pass

class Engine:

    def __init__(self, difficulty, scene_map):
        pass

    def play(self):
        pass

if __name__ == "__main__":
    print("What's your player's name?")
    name = input("> ")

    print("Are you playing on easy, medium or hard?")
    difficulty = input("> ")

    map = Map(bedroom, difficult)

    game = Engine(difficulty, map)

