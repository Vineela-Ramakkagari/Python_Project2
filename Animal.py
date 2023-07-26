
# Creating a base class Animal with a method make_sound().
class Animal:
    def make_sound(self):
        print("Generic animal sound")

# Creating two subclasses Dog and Cat, each inheriting from the Animal class.
class Dog(Animal):
    # Override the make_sound() method in the Dog class with its respective sound (bark).
    def make_sound(self):
        print("Bark!")

class Cat(Animal):
    # Override the make_sound() method in the Cat class with its respective sound (meow).
    def make_sound(self):
        print("Meow!")

# Implement a function called animal_sound_in_zoo() that takes an animal object as a parameter and calls its make_sound() method.
def animal_sound_in_zoo(animal):
    animal.make_sound()

# Creating instances of Dog and Cat classes and call the animal_sound_in_zoo() function with these instances as arguments to observe their unique sounds.
if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

    animal_sound_in_zoo(dog)  
    animal_sound_in_zoo(cat)  
