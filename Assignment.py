# The Parent Class
class Human:
    """A general human being with basic properties."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        """A generic greeting."""
        return f"Hello, my name is {self.name}."

# The Child Class, inheriting from Human
class Superhero(Human):
    """A superhero with special abilities, inheriting from Human."""
    def __init__(self, name, age, alias, superpower, power_level):
        # Call the parent class's constructor
        super().__init__(name, age)
        
        # New attributes for the Superhero class
        self.alias = alias
        self.superpower = superpower
        
        # A private attribute to demonstrate encapsulation
        self.__power_level = power_level

    # Polymorphism: Overriding the parent's greet method
    def greet(self):
        """A superhero-specific greeting, overriding the parent method."""
        return f"Greetings! I am {self.alias}, and I possess the power of {self.superpower}."
        
    def use_superpower(self):
        """A method to use the superhero's unique ability."""
        if self.__power_level > 50:
            print(f"{self.alias} unleashes their {self.superpower} with great force!")
        else:
            print(f"{self.alias} tries to use their {self.superpower}, but the power level is too low.")
    
    # Encapsulation: A method to safely access the private attribute
    def get_power_level(self):
        """Returns the private power level."""
        return self.__power_level

# --- Creating and using objects ---

# Create a regular Human object
citizen = Human("Alex", 30)

# Create a Superhero object
captain_code = Superhero("John Doe", 25, "Captain Code", "Debug-vision", 95)

# Demonstrate polymorphism with the greet method
print(citizen.greet())
print(captain_code.greet())

print("-" * 30)

# Demonstrate a superhero-specific method
captain_code.use_superpower()

# Demonstrate encapsulation by accessing the private attribute through a public method
print(f"Captain Code's current power level is: {captain_code.get_power_level()}")

# Attempting to directly access the private attribute will cause an error
try:
    print(captain_code.__power_level)
except AttributeError as e:
    print(f"\nCaught an error: {e}")
    print("This shows that __power_level is private and can't be accessed directly.")
