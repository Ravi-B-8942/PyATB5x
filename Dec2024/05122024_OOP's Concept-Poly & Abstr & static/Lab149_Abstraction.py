from abc import ABC, abstractmethod


class animal(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):          # by abstract method we are hiding this step in the class.
        pass


class dog(animal):

    def make_sound(self):
        print("Bark")


s_dog = dog("Tony")
s_dog.make_sound()
