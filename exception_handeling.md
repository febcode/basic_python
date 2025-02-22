# **Exception Handling in Python**
Exception handling allows you to gracefully handle errors and prevent program crashes.

---

## **1. What is an Exception?**
An **exception** is an error that occurs during execution. Examples:
- **ZeroDivisionError** – Dividing by zero  
- **FileNotFoundError** – File does not exist  
- **TypeError** – Invalid type operation  
- **KeyError** – Accessing a non-existent dictionary key  

---

## **2. Handling Exceptions Using `try-except`**
### **Basic Syntax**
```python
try:
    # Code that may raise an exception
    x = 5 / 0  # Raises ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")
```
✅ **Output:** `Cannot divide by zero!` (instead of crashing)

---

## **3. Handling Multiple Exceptions**
```python
try:
    x = int("abc")  # Raises ValueError
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid conversion to integer!")
```
✅ Catches `ValueError` and prints `Invalid conversion to integer!`.

---

## **4. Catching Multiple Exceptions in One Block**
```python
try:
    x = 5 / 0
except (ZeroDivisionError, ValueError) as e:
    print(f"Error occurred: {e}")
```
✅ Catches multiple exceptions in one block.

---

## **5. Using `else` for Code That Runs if No Exception Occurs**
```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Success:", x)
```
✅ Runs `else` block if no error occurs.

---

## **6. Using `finally` for Cleanup**
The `finally` block **always executes**, even if an exception occurs.

```python
try:
    file = open("sample.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("Closing file (if open)")
    file.close()  # This executes regardless of an exception
```

✅ Ensures resources (like files or DB connections) are closed.

---

## **7. Raising Custom Exceptions Using `raise`**
You can manually raise exceptions using `raise`.

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return f"Age is {age}"

print(set_age(25))  # ✅ Works fine
print(set_age(-5))  # ❌ Raises ValueError
```
✅ Raises a custom `ValueError`.

---

## **8. Custom Exception Classes**
Define custom exceptions for specific cases.

```python
class NegativeValueError(Exception):
    pass

def withdraw(amount):
    if amount < 0:
        raise NegativeValueError("Cannot withdraw negative amount")

try:
    withdraw(-100)
except NegativeValueError as e:
    print(f"Custom Exception: {e}")
```
✅ Useful for custom application logic.

---

## **9. Handling Exceptions in Loops**
```python
while True:
    try:
        num = int(input("Enter a number: "))
        print("You entered:", num)
        break
    except ValueError:
        print("Invalid input, please enter a number.")
```
✅ Keeps asking for input until a valid number is entered.

---

## **10. Summary Table**
| **Concept** | **Usage** |
|------------|----------|
| `try-except` | Handle exceptions |
| `except Exception as e` | Capture error details |
| `try-except-else` | Runs `else` if no exception |
| `try-finally` | Executes `finally` block always |
| `raise` | Manually throw exceptions |
| Custom Exception | Define app-specific errors |

