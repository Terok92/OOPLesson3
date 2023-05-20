from BMW import BMW
from Ferrari import Ferrari

bmw = BMW(220, "black", "sedan")
ferrari = Ferrari(250, "Red", "cabriolet", ":\tYes")

print("Is speed exceeded: " + bmw.is_speed_exceeded())
print(bmw.get_color())
print(bmw.get_type())

print("Is speed exceeded: " + ferrari.is_speed_exceeded())
print(ferrari.get_color())
print(ferrari.get_type())
print(ferrari.get_convertible())

print("\n")