# class Multiplier:
#     def __init__(self,factor):
#         self.factor= factor
#     def __call__(self, number):
#         # this method allows the objectto be called like a function 
#         return number * self.factor
# # creating an instanceof Multiplier with a factor of 5
#     multiplier = Multiplier(5)
# # Testing with callable() to check if the object is allable 
# print(callable(multiplier))
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        # This method allows the object to be called like a function
        return number * self.factor

# Creating an instance of Multiplier with a factor of 5
multiplier = Multiplier(5)

# Testing with callable() to check if the object is callable
print(callable(multiplier))  # Output: True

# Calling the instance like a function
print(multiplier(10))  # Output: 50
