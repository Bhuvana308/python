class Parent:
    def __init__(self,name):
        self.name = name

    def greet(self):
        return f"Hello, ny mane is {self.name}"

class Child(Parent):
    def child(self):
        print("this is child class")

    def greet(self, age=10):
        parent_greeting = super().greet()
        
