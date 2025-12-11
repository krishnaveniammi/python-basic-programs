class Grandfather:
    def own_house(self):
        print("I own a house.")

class Father(Grandfather):
    def own_bike(self):
        print("I own a bike.")

class Son(Father):
    def own_book(self):
        print("I own a book.")

# Create an object of the Son class
son_obj = Son()

# The son can access methods from all ancestor classes
son_obj.own_house()  # Output: I own a house.
son_obj.own_bike()   # Output: I own a bike.
son_obj.own_book()   # Output: I own a book.
