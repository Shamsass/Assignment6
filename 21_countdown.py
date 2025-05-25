# class Countdown:
#    def __init__(self,start):
#       self.start =start #set the starting number
#       self.current =start #initialize the current to starting number 
#    def __iter___(self):
#       return self 
   
#    def __next__(self):
#     # if current is less than 0,stop the iteration
#     if self.current<0:
#        raise StopIteration
#     # Decrease current by 1 and return the value 
#     self.current -= 1
#     return self.current +1 #return the number before decrementing
# #    creating an object of countdown 
# countdown = Countdown(5)
# # using the countdown object in a loop
# for number in countdown:
#    print(number)
      
class Countdown:
    def __init__(self, start):
        self.start = start          # Set the starting number
        self.current = start        # Initialize current to starting number

    def __iter__(self):             # Corrected here
        return self

    def __next__(self):
        # If current is less than 0, stop the iteration
        if self.current < 0:
            raise StopIteration
        # Decrease current by 1 and return the value
        self.current -= 1
        return self.current + 1     # Return the number before decrementing

# Creating an object of Countdown
countdown = Countdown(5)

# Using the countdown object in a loop
for number in countdown:
    print(number)
