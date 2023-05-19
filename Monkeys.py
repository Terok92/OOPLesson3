from alls import Animal


class Monkey(Animal):
    def __init__(self, name, age, foot_count):
        Animal.__init__(self, name, age, foot_count)
        self.sound = "haf-haf"

    def info(self):
        print(f"I am a monkey. My name is {self.name}. I am {self.age} years old.")

    def fact(self):
        print("I'm a shimpanze")

    def make_sound(self):
        print(self.sound)