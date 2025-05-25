
class Dog: 
    def __init__(self, name, breed):
        self.name = name 
        self.breed = breed  # instance variable

    def bark(self): 
        print(f"{self.name} is barking!")  

if __name__ == "__main__":
    # creating object (instance)
    my_dog = Dog("Tommy", "Labrador")
    # call the method
    my_dog.bark()
