class Pet:
    def __init__(self, name, age, breed):
        self._name = name
        self._age = age
        self._breed = breed

    def speak(self):
        pass

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_breed(self):
        return self._breed

    def describe(self):
        print(f"{self.get_name()} is a {self.get_age()}-year-old {self.get_breed()}")


class Cat(Pet):
    def speak(self):
        print("Meow!")

    def take_nap(self):
        print("Go away, I'm sleeping.")


class Dog(Pet):
    def speak(self):
        print("Woof!")

    def fetch(self, thing):
        print(f"You threw a {thing} and I went and got it!")


pet = Pet("Tom", 5, "Python")
cat = Cat("Whiskers", 3, "Calico")
dog = Dog("Buster", 7, "Rottweiler")
pet.describe()  # prints "My name is Tom, I am 5 years old, and I am a Python."
cat.describe()  # prints "My name is Whiskers, I am 3 years old, and I am a Tabby."
dog.describe()  # prints "My name is Fido, I am 7 years old, and I am a Labrador."
dog.fetch("golf club")
cat.take_nap()

