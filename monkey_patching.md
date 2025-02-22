# **Monkey Patching in Python 🐒🔧**  

**Monkey patching** refers to **modifying or extending code at runtime** without altering the original source code. This is commonly used to:  
- Fix bugs in third-party libraries.  
- Modify behavior dynamically.  
- Add new functionality to existing classes or modules.  

---

## **1. Basic Example: Modifying a Class Method at Runtime**
Let's modify an existing method **without modifying the class definition**.

### **Example: Changing a Method at Runtime**
```python
class Person:
    def greet(self):
        return "Hello!"

# Define a new function to replace the existing method
def new_greet(self):
    return "Hey there! Monkey patching at work!"

# Apply monkey patch
Person.greet = new_greet

p = Person()
print(p.greet())  # "Hey there! Monkey patching at work!"
```
✅ **We replaced the `greet` method dynamically** without changing the class definition.

---

## **2. Monkey Patching a Built-in Class**
You can also **modify built-in classes**.

### **Example: Adding a Method to `str` Class**
```python
def shout(self):
    return self.upper() + "!!!"

# Monkey patch str class
str.shout = shout

print("hello".shout())  # "HELLO!!!"
```
✅ **We extended the `str` class** by adding a new method `shout()`.

---

## **3. Patching a Third-Party Library (Example: `requests`)**
You can **modify external libraries** on the fly.

### **Example: Patching `requests.get()`**
```python
import requests

# Original function
original_get = requests.get

# Define a fake response function
def fake_get(url, *args, **kwargs):
    class FakeResponse:
        status_code = 200
        def json(self):
            return {"message": "Monkey patched!"}
    return FakeResponse()

# Apply the patch
requests.get = fake_get

# Test the patched function
response = requests.get("http://example.com")
print(response.json())  # {'message': 'Monkey patched!'}

# Restore the original function
requests.get = original_get
```
✅ **We intercepted `requests.get()` and returned a fake response** without modifying the library.

---

## **4. Using `unittest.mock.patch` (Safer Approach)**
Instead of permanent monkey patching, you can use **mocking** for temporary patches.

### **Example: Using `patch()` from `unittest.mock`**
```python
from unittest.mock import patch
import requests

def fake_get(url, *args, **kwargs):
    return {"message": "Patched response"}

with patch("requests.get", fake_get):
    print(requests.get("http://example.com"))  # {'message': 'Patched response'}
```
✅ **The original function remains unchanged outside the `with` block**.

---

## **5. When to Use Monkey Patching?**
✅ **Good Use Cases:**
- Fixing bugs in third-party libraries.  
- Overriding behavior in **testing and debugging**.  
- Adding missing functionality dynamically.  

❌ **Avoid When:**
- It makes the code harder to maintain.  
- There are **better alternatives** like subclassing or decorators.  
- It **modifies built-in classes** in an unexpected way.  

---

### **Final Thought**
Monkey patching is a powerful but **risky technique**. If used improperly, it can lead to **hard-to-debug issues**. Always prefer **mocking (`unittest.mock.patch`)** when working with test cases.

Would you like an **example of a real-world bug fix using monkey patching**? 🚀
