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


# What is namespace:
A namespace is a system that has a unique name for each and every object in Python. An object might be a variable or a method. Python itself maintains a namespace in the form of a Python dictionary. Let’s go through an example, a directory-file system structure in computers. Needless to say, that one can have multiple directories having a file with the same name inside every directory. But one can get directed to the file, one wishes, just by specifying the absolute path to the file. 
Real-time example, the role of a namespace is like a surname. One might not find a single “Alice” in the class there might be multiple “Alice” but when you particularly ask for “Alice Lee” or “Alice Clark” (with a surname), there will be only one (time being don’t think of both first name and surname are same for multiple students).
On similar lines, the Python interpreter understands what exact method or variable one is trying to point to in the code, depending upon the namespace. So, the division of the word itself gives a little more information. Its Name (which means name, a unique identifier) + Space(which talks something related to scope). Here, a name might be of any Python method or variable and space depends upon the location from where is trying to access a variable or a method.

## Types of namespaces :
 
When Python interpreter runs solely without any user-defined modules, methods, classes, etc. Some functions like print(), id() are always present, these are built-in namespaces. When a user creates a module, a global namespace gets created, later the creation of local functions creates the local namespace. The built-in namespace encompasses the global namespace and the global namespace encompasses the local namespace

## Scope of Objects in Python :
 
Scope refers to the coding region from which a particular Python object is accessible. Hence one cannot access any particular object from anywhere from the code, the accessing has to be allowed by the scope of the object.
Let’s take an example to have a detailed understanding of the same: 

```
# Python program showing
# a scope of object

def some_func():
	print("Inside some_func")
	def some_inner_func():
		var = 10
		print("Inside inner function, value of var:",var)
	some_inner_func()
	print("Try printing var from outer function: ",var)
some_func()

output: 
Inside some_func
Inside inner function, value of var: 10
print("Try printing var from outer function: ",var)
NameError: name 'var' is not defined
```

# Understanding Global Variables
Global variables are declared outside of any function or class and are accessible anywhere in the module. They retain their values throughout the execution of the program unless explicitly modified.

```
# Global variable
count = 10

def update_count():
    global count
    count += 5

update_count()
print(count)  # Output: 15

# This will raise an UnboundLocalError
count = 10

def update_count():
    count += 5  # Attempting to modify without declaring as global

update_count()

```
### **Access Specifiers in Python**
Access specifiers (also called **access modifiers**) in Python define the visibility and accessibility of class attributes and methods. Unlike other languages like Java or C++, Python does not enforce strict access control but follows naming conventions.

---

### **Types of Access Specifiers in Python**
| **Specifier** | **Syntax** | **Access** |
|--------------|-----------|------------|
| **Public** | `self.var` | Accessible everywhere |
| **Protected** | `self._var` | Accessible within the class and subclasses |
| **Private** | `self.__var` | Accessible only within the class (Name Mangling applies) |

---

# **1. Public Access Specifier**
- Any class attribute or method defined without an underscore (`_`) is **public**.
- It can be accessed anywhere, even outside the class.

```python
class Car:
    def __init__(self, brand):
        self.brand = brand  # Public attribute

    def display(self):  # Public method
        return f"Car brand: {self.brand}"

car = Car("Toyota")
print(car.brand)  # ✅ Accessible
print(car.display())  # ✅ Accessible
```

---

## **2. Protected Access Specifier (`_single_underscore`)**
- A **protected** attribute/method is prefixed with a **single underscore (`_`)**.
- It is **conventionally** meant to be used only within the class and subclasses.
- However, it can still be accessed from outside (not strictly enforced).

```python
class Vehicle:
    def __init__(self, brand):
        self._brand = brand  # Protected attribute

    def _display(self):  # Protected method
        return f"Vehicle brand: {self._brand}"

class Car(Vehicle):
    def show(self):
        return f"Car brand: {self._brand}"  # Accessible in subclass

car = Car("Honda")
print(car.show())  # ✅ Accessible in subclass
print(car._brand)  # ⚠️ Not recommended but still accessible
print(car._display())  # ⚠️ Not recommended but still accessible
```
🔹 **Python does not strictly enforce protected access.** It's just a naming convention.

---

## **3. Private Access Specifier (`__double_underscore`)**
- A **private** attribute/method is prefixed with **double underscores (`__`)**.
- It cannot be directly accessed outside the class.
- Python uses **name mangling** (`_ClassName__var`) to make it inaccessible from outside.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def __secret_method(self):  # Private method
        return "This is a secret method"

    def get_balance(self):  # Public method to access private data
        return self.__balance

account = BankAccount(1000)

# print(account.__balance)  # ❌ AttributeError: Cannot access private variable
# print(account.__secret_method())  # ❌ AttributeError: Cannot access private method

print(account.get_balance())  # ✅ Correct way to access private attribute

# Accessing using name mangling (not recommended)
print(account._BankAccount__balance)  # ⚠️ Not recommended but works
print(account._BankAccount__secret_method())  # ⚠️ Not recommended but works
```

🔹 **Python does not have true private variables**, but name mangling makes it harder to access them.

---

## **Access Specifiers Summary**
| **Specifier** | **Usage** | **Accessible in** | **Enforced?** |
|-------------|----------|----------------|------------|
| **Public (`self.var`)** | Default access | Everywhere | No |
| **Protected (`self._var`)** | Internal use | Class & subclasses | No (only convention) |
| **Private (`self.__var`)** | Hide implementation details | Only within class (name mangling) | Partially (via name mangling) |

---

## **When to Use Access Specifiers?**
- **Public (`self.var`)** → When the attribute/method should be freely accessible.
- **Protected (`self._var`)** → When it is intended for internal use within the class and subclasses.
- **Private (`self.__var`)** → When you want to hide implementation details from outside access.

