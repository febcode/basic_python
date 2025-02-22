# **Getters and Setters in Python**  

In Python, **getters and setters** are used to control access to instance variables in a class. Unlike some other languages (like Java),
Python does not enforce strict encapsulation, but we can use **properties** to achieve controlled access.

---

## **1. Without Getters and Setters**  
By default, Python allows direct access to instance variables:  

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  # Public attribute

p = Person("Alice", 25)
print(p.age)  # ✅ Direct access (not recommended in some cases)
p.age = 30  # ✅ Direct modification
print(p.age)  # 30
```
✅ **Issue:** No validation or control over the `age` attribute.

---

## **2. Using Getters and Setters (Traditional Method)**
A common way to **restrict direct access** is to use **getter and setter methods**.

```python
class Person:
    def __init__(self, name, age):
        self._name = name      # Protected variable (_name)
        self._age = age        # Protected variable (_age)

    def get_age(self):  # Getter
        return self._age

    def set_age(self, age):  # Setter
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age

p = Person("Alice", 25)
print(p.get_age())  # ✅ Accessing using getter

p.set_age(30)       # ✅ Modifying using setter
print(p.get_age())  # 30

# p.set_age(-5)  # ❌ Raises ValueError: Age cannot be negative
```
✅ **Benefit:** We can add validation inside `set_age()`.

---

## **3. Using `@property` (Pythonic Way)**
Python provides a **more elegant way** to define getters and setters using the `@property` decorator.

```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):  # Getter
        return self._age

    @age.setter
    def age(self, age):  # Setter
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age

p = Person("Alice", 25)
print(p.age)  # ✅ Uses the getter (no parentheses needed)

p.age = 30    # ✅ Uses the setter
print(p.age)  # 30

# p.age = -5  # ❌ Raises ValueError
```
✅ **Why is this better?**  
- Looks **more natural** (`p.age` instead of `p.get_age()`)  
- **Prevents direct modification** of `_age`  
- Allows **read-only** properties if needed  

---

## **4. Read-Only Property**
If you only define a **getter** (no setter), the property becomes **read-only**.

```python
class Car:
    def __init__(self, model):
        self._model = model

    @property
    def model(self):  # Read-only property
        return self._model

c = Car("Tesla")
print(c.model)  # ✅ Allowed

# c.model = "BMW"  # ❌ Raises AttributeError (no setter defined)
```
✅ **Use Case:** When a value **should not change** after initialization.

---

## **5. Private Attributes with Getters and Setters**
While Python does not have **true private variables**, we can indicate private attributes with **double underscores (`__var`)**.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    @property
    def balance(self):  # Getter
        return self.__balance

    @balance.setter
    def balance(self, amount):  # Setter
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount

acc = BankAccount(1000)
print(acc.balance)  # ✅ Works

acc.balance = 500  # ✅ Modifies balance
print(acc.balance)  # 500

# print(acc.__balance)  # ❌ AttributeError: Cannot access private variable
```
✅ **Key Point:**  
- `__balance` is **private** and cannot be accessed directly.  
- We use `@property` and `@balance.setter` to **control modifications**.

---

## **6. When to Use Getters and Setters?**
| **Scenario** | **Solution** |
|-------------|-------------|
| Simple attributes with no validation | ✅ Direct access (`self.var`) |
| Need to **validate data before setting** | ✅ Use setters (`@property`) |
| Need to make an attribute **read-only** | ✅ Define only a getter (`@property`) |
| Need to enforce **encapsulation** | ✅ Use private attributes (`__var`) |

---

## **Final Thoughts**
- ✅ **Use direct access for simple attributes.**  
- ✅ **Use `@property` for better control and validation.**  
- ✅ **Make attributes read-only if they should not be modified.**  
- ✅ **Use private variables (`__var`) when necessary.**  

