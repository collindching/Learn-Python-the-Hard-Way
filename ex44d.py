class Parent:

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def override(selfself):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

## instantiate dad and son
dad = Parent()
son = Child()

## calls Parent.implicit()
dad.implicit()
## calls Parent.implicit()
son.implicit()

## calls Parent.override()
dad.override()
## overridden by Child class
son.override()

dad.altered()
## overridden by Child class, using altered() function from Parent
son.altered()