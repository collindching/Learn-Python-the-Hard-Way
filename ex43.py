from sys import exit
from random import randint

class Scene:

    def enter(self):
        pass

class Engine:

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print("\n--------")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self):
        print(Death.quips[randint(0,len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print("The Gothons of Planet Percal #25 have invaded your ship and destroyed")
        print("your entire crew. You are the last surviving member and your last")
        print("mission is to get the neutron destruct bomb from the Weapons Armory,")
        print("put it in the bridge, and blow the ship up after getting into an ")
        print("escape pod.")
        print("\n")
        print("You're running down the central corridor to the Weapons Armory when")
        print("a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume")
        print("flowing around his hate filled body. He's blocking the door to the")
        print("Armory and about to pull a weapon to blast you.")

        action = input("> ")

        if action == "shoot!":
            print("Quick on the draw, you yank out your blaster and fire at the Gothon.")
            print("Your laser hits his costume but misses him entirely.")
            print("He flies into a rage and blasts you repeatedly in the face until you die.")
            return 'death'

        elif action == "tell a joke":
            print("You tell the one Gothon joke you know.")
            print("The Gothon stops, tries not to laugh, and busts out laughing and can't move.")
            print("You shoot him square in the head, putting him down.")
            print("Then you jump through the Weapon Armory door.")
            return 'laser_weapon_armory'

        elif action == "42":
            return('escape_pod')

        else:
            print("Does not compute!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print("You do a dive roll into the Weapon Armory, crouch and scan the room")
        print("for more Gothons. It's dead quiet, too quiet.")
        print("You run to the far sid eof the room and find the")
        print("neutron bomb in its container. There's a keypad lock on the box")
        print("and you need the code to get the bomb out. If you get the code")
        print("wrong 10 times then the lock closes forever and you can't")
        print("get the bomb. The code is 3 digits.")
        code = "%d%d%d" % (1,2,3)
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print("The container clicks opena nd the seal breaks.")
            print("You grab the neutron bomb and run to the")
            print("bridge where you must place it in the right spot.")
            return 'the_bridge'

        else:
            print("The lock buzzes one last time and then you hear a sickening")
            print("melting sound as the mechanism is fused together.")
            print("The Gothons blow up the ship and you die.")
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print("You burst onto the Bridge with the neutron destruct bomb")
        print("under your arm and surprise 5 Gothons who are trying to")
        print("take control of the ship. They haven't pulled their")
        print("weapons out yet, as they see the active bomb under your")
        print("arm and don't want to set it off.")

        action = input("> ")

        if action == "throw the bomb":
            print("In a panic you throw the bomb at the group of Gothons")
            print("and make a leap for the door. Right as you drop it a")
            print("Gothon shoots you right in the back, killing yuou.")
            print("As you die you see another Gothon frantically try to disarm")
            print("the bomb. You die knowing they will probably blow up.")

            return 'death'

        elif action == "slowly place the bomb":
            print("You point your blaster at the bomb under your arm")
            print("and the Gothons put their hands up and start to sweat.")
            print("You inch backward to the door, open it, and then carefully")
            print("place the bomb on the floor, pointing your blaster at it.")
            print("You then jump back through the door, punch the close button")
            print("and blast the lock so the Gothons can't get out.")
            print("Now that the bomb is placed you run to the escape pod to")
            print("get off this tin can.")
            return 'escape_pod'

        else:
            print('Does not compute!')
            return('the_bridge')

class EscapePod(Scene):

    def enter(self):
        print("You rush through the ship to make it to to the escape")
        print("pod before the whole ship explodes. It seems like")
        print("hardly any Gothons are on the ship. You get to the")
        print("chamber with escape pods, and now need to pick")
        print("one to take. Some of them could be damaged but")
        print("you don't have time to look. There's 5 pods.")
        print("Which one do you take?")

        good_pod = 3
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print("You jump into pod %s and hit the eject button." % guess)
            print("The pod escapes out into the void of space, then")
            print("implodes as the hull ruptures.")
            return 'death'
        else:
            print("You jump into pod %s and hit the eject button." % guess)
            print("The pod easily slides out into space heading to")
            print("the planet below. As it flies to the planet, you look")
            print("back and see your ship implode then explode like a")
            print("bright star, taking out the Gothon ship at the same")
            print("time. You won!")
            exit(1)

class Map:

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes[scene_name]

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
