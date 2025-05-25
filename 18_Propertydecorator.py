# class Product:
#       def __init__(self, name ,price):
#             self.name=name
#             self.__price =price    #private attribute 

#     # Getter for the price attribute
# @property
# def price(self):
#       return self._price
# # Setter to update the price attribute
# @price.setter
# def price(self,value):
#       if value <0:
#          print("Price can not be negative!")
#       else:
#          self. _price =value
#         #  deleter to delete the price attribute
# @price.deleter
# def price(self):
#      print(f"Deletingthe price of {self.name}")
#      del self._price
# # creating a product  object
# product =Product("Laptop", 1000)
# # Accessingthe price using the @property
# print(product.price)
# # updating the price using the @price.setter
# product.price =1200
# print(product.price)


# # Trying to set a negativeprice 
# product.price = -500
# # deletingthe price  using @price.deleter
# del product.price 
class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Use _price to match the property methods

    # Getter for the price attribute
    @property
    def price(self):
        return self._price

    # Setter to update the price attribute
    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            self._price = value

    # Deleter to delete the price attribute
    @price.deleter
    def price(self):
        print(f"Deleting the price of {self.name}")
        del self._price

# Creating a Product object
product = Product("Laptop", 1000)

# Accessing the price using the @property
print(product.price)

# Updating the price using the @price.setter
product.price = 1200
print(product.price)

# Trying to set a negative price 
product.price = -500  # Should print warning

# Deleting the price using @price.deleter
del product.price
