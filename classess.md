# Python Classes and Objects

A class in Python is a user-defined template for creating objects. 
It bundles data and functions together, making it easier to manage and use them. 
When we create a new class, we define a new type of object. We can then create multiple instances of this object type.

Classes are created using class keyword. 
Attributes are variables defined inside the class and represent the properties of the class. 
Attributes can be accessed using the dot . operator (e.g., MyClass.my_attribute).
```
# define a class
class Dog:
    sound = "bark"  # class attribute

# Create an object from the class
#sound attribute is a class attribute. It is shared across all instances of Dog class, so can be directly accessed through instance dog1.
dog1 = Dog()

# Access the class attribute
print(dog1.sound)
```

## Using __init__() Function
In Python, class has __init__() function. It automatically initializes object attributes when an object is created.

```
class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute 
        self.age = age  # Instance attribute

    def bark(self):
        print(self.name)

    def __str__(self):
        return f"{self.name} is {self.age} years old."  # Correct: Returning a string

# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

# Output
# Buddy is 3 years old.
# Charlie is 5 years old.

print(dog1.name)  # Output: Buddy   -  (Instance variable)
print(dog1.species)  # Output: Canine -  (Class variable)

# Modify instance variables
dog1.name = "Max"
print(dog1.name)     # (Updated instance variable)

# Modify class variable
Dog.species = "Feline"
print(dog1.species)  # (Updated class variable)
print(dog2.species)

```

## Explanation:

**class Dog:** Defines a class named Dog.
**species:** A class attribute shared by all instances of the class.
**__init__ method:** Initializes the name and age attributes when a new object is created.
**dog1.name:** Accesses the instance attribute name of the dog1 object.
**dog1.bark():** Calls the bark method on dog1.
**_str__ Method ** in Python allows us to define a custom string representation of an object. 
By default, when we print an object or convert it to a string using str(), Python uses the default implementation,
which returns a string like <__main__.ClassName object at 0x00000123>.

## Class and Instance Variables in Python
In Python, variables defined in a class can be either class variables or instance variables, 
and understanding the distinction between them is crucial for object-oriented programming.

### Class Variables
These are the variables that are shared across all instances of a class. It is defined at the class level, outside any methods.
All objects of the class share the same value for a class variable unless explicitly overridden in an object.

### Instance Variables
Variables that are unique to each instance (object) of a class. These are defined within __init__ method or other instance methods. 
Each object maintains its own copy of instance variables, independent of other objects.

## Explanation:

1. Class Variable (species): Shared by all instances of the class. Changing Dog.species affects all objects, as it’s a property of the class itself.
2. Instance Variables (name, age): Defined in the __init__ method. Unique to each instance (e.g., dog1.name and dog2.name are different).
3. Accessing Variables: Class variables can be accessed via the class name (Dog.species) or an object (dog1.species).
   Instance variables are accessed via the object (dog1.name).
5. Updating Variables: Changing Dog.species affects all instances. Changing dog1.name only affects dog1 and does not impact dog2





