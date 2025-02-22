#Inheritance is a key feature of Object-Oriented Programming (OOP) in Python that allows a class (child class) to inherit attributes and methods from another class (parent class). 
This promotes code reusability and a hierarchical class structure.

## **Types of Inheritance in Python**
### 1. **Single Inheritance**
   - One child class inherits from one parent class.
   ```python
   class Parent:
       def func1(self):
           print("This is a parent class")

   class Child(Parent):
       def func2(self):
           print("This is a child class")

   obj = Child()
   obj.func1()  # Inherited from Parent
   obj.func2()
   ```

### 2. **Multiple Inheritance**
   - A child class inherits from multiple parent classes.
   ```python
   class Parent1:
       def func1(self):
           print("This is Parent1")

   class Parent2:
       def func2(self):
           print("This is Parent2")

   class Child(Parent1, Parent2):
       def func3(self):
           print("This is Child")

   obj = Child()
   obj.func1()
   obj.func2()
   obj.func3()
   ```

### 3. **Multilevel Inheritance**
   - A child class inherits from another child class.
   ```python
   class Grandparent:
       def func1(self):
           print("This is Grandparent")

   class Parent(Grandparent):
       def func2(self):
           print("This is Parent")

   class Child(Parent):
       def func3(self):
           print("This is Child")

   obj = Child()
   obj.func1()
   obj.func2()
   obj.func3()
   ```

### 4. **Hierarchical Inheritance**
   - Multiple child classes inherit from a single parent class.
   ```python
   class Parent:
       def func1(self):
           print("This is Parent")

   class Child1(Parent):
       def func2(self):
           print("This is Child1")

   class Child2(Parent):
       def func3(self):
           print("This is Child2")

   obj1 = Child1()
   obj1.func1()
   obj1.func2()

   obj2 = Child2()
   obj2.func1()
   obj2.func3()
   ```

### 5. **Hybrid Inheritance**
   - A combination of multiple types of inheritance.
   ```python
   class A:
       def func1(self):
           print("This is class A")

   class B(A):
       def func2(self):
           print("This is class B")

   class C(A):
       def func3(self):
           print("This is class C")

   class D(B, C):  # Multiple + Multilevel Inheritance
       def func4(self):
           print("This is class D")

   obj = D()
   obj.func1()
   obj.func2()
   obj.func3()
   obj.func4()
   ```

## **Method Overriding**
When a child class provides a different implementation of a method that is already defined in the parent class.

```python
class Parent:
    def show(self):
        print("This is the parent class")

class Child(Parent):
    def show(self):  # Overriding method
        print("This is the child class")

obj = Child()
obj.show()  # Calls the overridden method in Child
```

## **Super() Function**
The `super()` function allows access to the parent class's methods.

```python
class Parent:
    def show(self):
        print("This is the parent class")

class Child(Parent):
    def show(self):
        super().show()  # Calls parent class method
        print("This is the child class")

obj = Child()
obj.show()
```

## **When to Use Inheritance?**
- When multiple classes share common behavior.
- When you want to follow the **DRY (Don't Repeat Yourself)** principle.
- When you need a hierarchical relationship among classes.

# **Method Resolution Order (MRO) in Python**
Method Resolution Order (MRO) determines the sequence in which classes are searched when executing a method. Python follows the **C3 Linearization (or C3 Algorithm)** for MRO.

To check the MRO of a class, use:
```python
print(ClassName.__mro__)  # OR
print(ClassName.mro())
```

#### **Example of MRO in Single Inheritance**
```python
class A:
    def show(self):
        print("A class")

class B(A):
    pass

obj = B()
obj.show()  # Output: A class
print(B.__mro__)  
```
**MRO Output:**  
`(<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)`

Since `B` does not have the `show()` method, Python looks for it in `A`, then in `object` (topmost class in Python).

---

#### **MRO in Multiple Inheritance**
```python
class A:
    def show(self):
        print("A class")

class B(A):
    def show(self):
        print("B class")

class C(A):
    def show(self):
        print("C class")

class D(B, C):  # Multiple Inheritance
    pass

obj = D()
obj.show()  # Output: B class
print(D.__mro__)  
```
**MRO Output:**
```
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```
- `D` looks for `show()`
- `B` has it, so it stops there.
- If `B` didn't have `show()`, it would search in `C`, then `A`, then `object`.

---

#### **Using `super()` in Multiple Inheritance**
```python
class A:
    def show(self):
        print("A class")

class B(A):
    def show(self):
        print("B class")
        super().show()  # Calls A's method

class C(A):
    def show(self):
        print("C class")
        super().show()  # Calls A's method

class D(B, C):
    def show(self):
        print("D class")
        super().show()  # Calls B's method

obj = D()
obj.show()
print(D.__mro__)
```
**Output:**
```
D class
B class
C class
A class
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```
- `super().show()` in `D` calls `B.show()`
- `super().show()` in `B` calls `C.show()`
- `super().show()` in `C` calls `A.show()`
- Stops at `A`, as `A` doesn’t call `super().show()`

---

### **Real-World Use Cases of Inheritance**
#### **1. User Management System**
```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def display(self):
        print(f"Name: {self.name}, Email: {self.email}")

class Admin(User):
    def __init__(self, name, email, admin_level):
        super().__init__(name, email)
        self.admin_level = admin_level

    def display(self):
        super().display()
        print(f"Admin Level: {self.admin_level}")

admin = Admin("Alice", "alice@example.com", "SuperAdmin")
admin.display()
```

#### **2. Shape Inheritance (Polymorphism)**
```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print(shape.area())  # Calls the correct area() based on the object type
```

### **Abstract Base Classes (ABC) in Python**
In Python, **Abstract Base Classes (ABC)** define a blueprint for other classes. They enforce method implementation in child classes using the `abc` module.

#### **Why Use ABC?**
- Ensures all child classes implement specific methods.
- Prevents instantiation of the base class if it is meant to be abstract.
- Helps maintain a consistent interface across different implementations.

---

### **Defining an Abstract Class**
Use the `abc.ABC` class and the `@abstractmethod` decorator.

```python
from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract Base Class
    @abstractmethod
    def sound(self):
        pass  # Must be implemented in child classes

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# obj = Animal()  # This will raise an error (cannot instantiate abstract class)
dog = Dog()
cat = Cat()

print(dog.sound())  # Output: Bark
print(cat.sound())  # Output: Meow
```
🔹 **Key points:**  
- The `Animal` class cannot be instantiated directly.  
- The `Dog` and `Cat` classes **must** implement `sound()`; otherwise, Python will raise an error.

---

### **Abstract Class with Constructor**
You can define instance variables in the abstract class.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def max_speed(self):
        pass

class Car(Vehicle):
    def max_speed(self):
        return 200

class Bike(Vehicle):
    def max_speed(self):
        return 100

car = Car("Toyota")
bike = Bike("Yamaha")

print(car.name, car.max_speed())  # Output: Toyota 200
print(bike.name, bike.max_speed())  # Output: Yamaha 100
```
---

### **Abstract Properties and Setters**
We can also enforce abstract properties.

```python
from abc import ABC, abstractmethod

class Person(ABC):
    @property
    @abstractmethod
    def role(self):
        pass

class Employee(Person):
    def __init__(self, role):
        self._role = role

    @property
    def role(self):
        return self._role

emp = Employee("Software Engineer")
print(emp.role)  # Output: Software Engineer
```
---

### **Metaclasses in Python**
A **metaclass** in Python is a class that defines the behavior of other classes (i.e., it controls how classes are created). Normally, classes are instances of `type`, but you can customize class creation by defining a metaclass.

#### **Basic Example of a Metaclass**
```python
class Meta(type):
    def __new__(cls, name, bases, class_dict):
        print(f"Creating class: {name}")
        return super().__new__(cls, name, bases, class_dict)

class MyClass(metaclass=Meta):
    def hello(self):
        return "Hello, Metaclass!"

obj = MyClass()
print(obj.hello())
```
🔹 **Key points:**
- When `MyClass` is defined, `Meta.__new__()` is called.
- You can modify class attributes or methods before the class is created.

---

### **Enforcing Abstract Methods Using a Metaclass**
```python
class AbstractMeta(type):
    def __init__(cls, name, bases, class_dict):
        super().__init__(name, bases, class_dict)
        if "process" not in class_dict:
            raise TypeError(f"Class {name} must define 'process' method")

class Base(metaclass=AbstractMeta):
    pass

class ValidClass(Base):
    def process(self):
        print("Processing...")

# class InvalidClass(Base):  # This will raise TypeError
#     pass

obj = ValidClass()
obj.process()  # Output: Processing...
```
---

### **Key Takeaways**
- **Abstract Base Classes (ABC):** Used to enforce method implementation in child classes.
- **Metaclasses:** Define how classes behave and can enforce rules at class creation time.
- **MRO (Method Resolution Order):** Determines method lookup sequence.
- **Super() in Multiple Inheritance:** Helps maintain method calling order.

# **Interfaces in Python**
Python doesn’t have a built-in `interface` keyword like Java or C#, but we can achieve **interface-like behavior** using **Abstract Base Classes (ABC)**.

---

### **What is an Interface?**
An **interface** defines a contract that a class must follow. It only declares methods that must be implemented in any class that inherits from it.

#### **Key Features of Interfaces:**
- They contain only method signatures (no implementation).
- They enforce implementation in subclasses.
- They allow multiple inheritance to define common behavior.

---

### **Defining an Interface Using ABC**
We can use `ABC` from the `abc` module to create an interface.

```python
from abc import ABC, abstractmethod

class Animal(ABC):  # Interface
    @abstractmethod
    def sound(self):
        pass  # No implementation

    @abstractmethod
    def move(self):
        pass  # No implementation

class Dog(Animal):
    def sound(self):
        return "Bark"

    def move(self):
        return "Runs on 4 legs"

class Bird(Animal):
    def sound(self):
        return "Chirp"

    def move(self):
        return "Flies in the sky"

dog = Dog()
bird = Bird()

print(dog.sound(), "-", dog.move())  # Output: Bark - Runs on 4 legs
print(bird.sound(), "-", bird.move())  # Output: Chirp - Flies in the sky
```
✅ **Why this is an Interface?**
- `Animal` class has only method signatures (no implementation).
- All child classes **must** implement `sound()` and `move()`.
- If a child class doesn’t implement all methods, Python will raise an error.

---

### **Python Interface with Multiple Inheritance**
Unlike Java or C#, Python allows multiple inheritance, so a class can implement multiple interfaces.

```python
from abc import ABC, abstractmethod

class Flyable(ABC):  # Interface
    @abstractmethod
    def fly(self):
        pass

class Swimmable(ABC):  # Interface
    @abstractmethod
    def swim(self):
        pass

class Duck(Flyable, Swimmable):
    def fly(self):
        return "Duck flies short distances"

    def swim(self):
        return "Duck swims in the pond"

duck = Duck()
print(duck.fly())  # Output: Duck flies short distances
print(duck.swim())  # Output: Duck swims in the pond
```
✅ **Why Use Multiple Interfaces?**
- A **Duck** is both `Flyable` and `Swimmable`, so it implements both.
- This helps achieve a clean design without forcing unrelated methods.

---

### **Dynamic Interface Checking with `isinstance()`**
We can check if a class implements an interface.

```python
print(isinstance(duck, Flyable))  # True
print(isinstance(duck, Swimmable))  # True
```

---

### **When to Use an Interface in Python?**
| **Scenario** | **Use ABC Interface?** |
|-------------|------------------|
| You want to enforce method implementation | ✅ Yes |
| You need multiple inheritance for behavior | ✅ Yes |
| You want to restrict class instantiation | ✅ Yes |
| You need a simple base class with default implementations | ❌ Use regular inheritance |

