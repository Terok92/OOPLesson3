from alls import Animal
from Monkeys import Monkey
from Donkeys import Donkey

just_animal = Animal("Shun", 23, 5)
wild_animal = Monkey("Kapik", 30, 2)
pet_animal = Donkey("Ishuk", 14, 4)

print(just_animal)
just_animal.fact()
print("\n")

for animal in (wild_animal, pet_animal):
    animal.make_sound()
    animal.info()
    animal.fact()
    animal.make_sound()
    print("\n")
