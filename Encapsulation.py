'''Using OOP in Python, we can restrict access to methods and variables. 
This prevent data from direct modification which is called encapsulation. 
In Python, we denote private attribute using underscore as prefix i.e single “ _ “ or double “ __“.'''
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# trying to change the price in below assignment, which was declarde in the constructor, but you cant do. and in the 
#function definition this value will remain as it is. although it can change in the object prospective.

c.__maxprice = 1000
c.sell()

# using setter function

c.setMaxPrice(1000)
c.sell()

# Creating new object and now the original value has been changed. Below are the new object.
d = Computer()
c.sell()


