class Person:
    def __init__(self, name, age):
        # Initialize using the setter method to apply validation immediately
        self.name = name
        self.age = age

    @property
    def name(self):
        """Getter method for the name attribute."""
        return self.__name # Access the private attribute

    @name.setter
    def name(self, value):
        """Setter method for the name attribute with validation."""
        if not value:
            raise ValueError("Name cannot be empty")
        self.__name = value # Set the private attribute

    @property
    def age(self):
        """Getter method for the age attribute."""
        return self.__age

    @age.setter
    def age(self, value):
        """Setter method for the age attribute with validation."""
        if not isinstance(value, int) or not (0 < value < 120):
            raise ValueError("Age must be a valid number between 0 and 120")
        self.__age = value

# Usage
try:
    person = Person("Alice", 30)
    print(f"Name: {person.name}, Age: {person.age}") # Access like an attribute (uses getter)

    person.age = 35 # Modify like an attribute (uses setter with validation)
    print(f"Updated Age: {person.age}")

    # This will raise a ValueError due to validation in the setter
    # person.age = 150 
    # person.name = ""

except ValueError as e:
    print(f"Error: {e}")
