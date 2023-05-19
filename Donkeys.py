from alls import Animal


class Donkey(Animal):
    def __init__(self, name, age, foot_count):
        Animal.__init__(self, name, age, foot_count)
        self.sound = "yo-yo"

    def info(self):
        print(f"I am a donkey. My name is {self.name}. I am {self.age} years old.")

    def fact(self):
        print("I'm the kind animal")

    def make_sound(self):
        print(self.sound)