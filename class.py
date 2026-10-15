class Bottle:
    def __init__(self, capacity, size, color, material):
        self.capacity = capacity
        self.size = size
        self.color = color
        self.material = material

    def fill(self):
        self.color = self.color.upper()
        print(f"The {self.color} bottle is filled withj liquid.")

    # def empty(self):
    #     self.is_filled = False
    #     print("The bottle is now empty.")

    # def drink(self):
    #     if self.is_filled:
    #         self.is_filled = False
    #         print("You drank the liquid.")
    #     else:
    #         print("The bottle is already empty!")

Bottle.fill
bottle1 = Bottle(500, "Medium", "Pink", "Plastic")
print(bottle1.capacity, bottle1.size, bottle1.color,bottle1.material)
print(f"Bottle1:{bottle1.size},{bottle1.color},{bottle1.material}")
bottle2 = Bottle(1000, "Large", "Green", "Glass")
bottle2.fill()
print(f"Bottle2:{bottle2.size},{bottle2.color},{bottle2.material}")
bottle3 = Bottle(100, "small", "red", "Glass")
bottle2.fill()
print(f"Bottle3:{bottle3.size},{bottle3.color},{bottle3.material}")

