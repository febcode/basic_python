# **Decorators in Python** 🏗️✨  

Decorators are a powerful feature in Python that **modify the behavior of functions or classes** without changing their code. They allow for cleaner, reusable, and more maintainable code.

---

## **1. What is a Decorator?**
A **decorator** is a function that **wraps another function** to extend or modify its behavior.

### **Basic Syntax:**
```python
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before the function call!")
        original_function()
        print("Wrapper executed after the function call!")
    return wrapper_function
```

---

## **2. Simple Function Decorator**
Let's create a decorator that **logs when a function runs**.

### **Example: Logging Decorator**
```python
def log_decorator(func):
    def wrapper():
        print(f"Calling function: {func.__name__}")
        func()
        print(f"Function {func.__name__} executed successfully!")
    return wrapper

@log_decorator  # Applying the decorator
def greet():
    print("Hello, World!")

greet()
```
### **Output:**
```
Calling function: greet
Hello, World!
Function greet executed successfully!
```
✅ The decorator runs **before and after** the `greet` function.

---

## **3. Decorators with Arguments**
If the original function **accepts arguments**, the decorator should handle them.

### **Example: Timing Function Execution**
```python
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute")
        return result
    return wrapper

@timer_decorator
def compute_sum(n):
    return sum(range(n))

print(compute_sum(1000000))
```
### **Output:**
```
compute_sum took 0.0356 seconds to execute
499999500000
```
✅ The decorator **measures execution time**.

---

## **4. Multiple Decorators**
You can apply **multiple decorators** to a function.

### **Example: Applying Two Decorators**
```python
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

def exclamation_decorator(func):
    def wrapper():
        result = func()
        return result + "!!!"
    return wrapper

@uppercase_decorator
@exclamation_decorator
def greet():
    return "hello"

print(greet())
```
### **Output:**
```
HELLO!!!
```
✅ The `exclamation_decorator` adds `"!!!"`, and `uppercase_decorator` converts it to uppercase.

---

## **5. Class-Based Decorators**
A **class can be used as a decorator** by implementing the `__call__` method.

### **Example: Class-Based Decorator**
```python
class RepeatDecorator:
    def __init__(self, times):
        self.times = times

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for _ in range(self.times):
                func(*args, **kwargs)
        return wrapper

@RepeatDecorator(3)
def say_hello():
    print("Hello!")

say_hello()
```
### **Output:**
```
Hello!
Hello!
Hello!
```
✅ The function **runs 3 times** because of the decorator.

---

## **6. Real-World Use Cases**
| **Use Case** | **Example Decorator** |
|-------------|----------------|
| **Logging** | `@log_decorator` (logs function calls) |
| **Authentication** | `@login_required` (checks if a user is logged in) |
| **Performance Profiling** | `@timer_decorator` (measures execution time) |
| **Caching Results** | `@lru_cache` (caches function results for optimization) |

---

## **7. Built-in Python Decorators**
Python has some **built-in decorators**:

| **Decorator** | **Purpose** |
|--------------|------------|
| `@staticmethod` | Defines a method that doesn't access instance data |
| `@classmethod` | Defines a method that gets the class as the first argument |
| `@property` | Creates getter/setter properties |

### **Example: `@property` Decorator**
```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

p = Person("Alice")
print(p.name)  # Alice
# p.name = "Bob"  # ❌ AttributeError (read-only)
```

---

## **Final Thoughts**
- ✅ **Use decorators** to enhance functions **without modifying their code**.  
- ✅ **Use `@decorator_name`** syntax for cleaner code.  
- ✅ **Use `*args` and `**kwargs`** to handle function arguments.  
- ✅ **Use class-based decorators** for complex behavior.  

