
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    # add the greet method to the class
    cls.greet = greet
    return cls

# applying the class decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):  # fixed typo here
        self.name = name

    def introduce(self):
        return f"Hi, I'm {self.name}"

# creating an instance of the Person class
person = Person("Alice")

# calling the greet method added by the decorator
print(person.greet())
