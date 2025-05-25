# custome exception
class InvalidAgeError(Exception):
    def __init__(self, message= "Age must be 18 or older"):
        self.message =message
        super().__init__(self.message)
# Function to check age 
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age : {age}.You must be 18 or or older.")
    else :
        print(f"Age{age}is valid!")
# Handling the exception using try ....except
try:
   age=int(input("Enter your age :"))
   check_age(age)
except InvalidAgeError as e:
    print(f"Error:{e}")
except ValueError:
    print("Please enter a valid integerfor age ")
