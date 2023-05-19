class Animal:
    def __init__(self, name, age, foot_count):
        self.age = age
        self.name = name
        self.foot_count = foot_count

    def __str__(self):
        return self.name

    def fact(self):
        print("All animals are equal")