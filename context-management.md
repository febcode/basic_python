### **Context Management in Python (`with` Statement)**
Context management in Python ensures that resources like **files, database connections, network sockets, etc.,** are properly acquired and released, even if an error occurs. 

The most common way to manage resources is by using the **`with` statement**, which automatically handles setup and cleanup.

---

## **1. Why Use Context Management?**
Without context management, you need to manually release resources:

```python
file = open("sample.txt", "r")  # Opening file
try:
    content = file.read()
    print(content)
finally:
    file.close()  # Manually closing file
```
⚠️ **Issue:** If an exception occurs, `file.close()` might not run.

### **Using `with` Statement (Best Practice)**
```python
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)  # File automatically closes after block
```
✅ **Advantages:**
- **Automatic cleanup** (no need to call `close()`)
- **Handles exceptions gracefully**
- **Shorter and cleaner code**

---

## **2. Context Management for Files**
```python
with open("output.txt", "w") as file:
    file.write("Hello, world!")
# File is automatically closed after this block
```

---

## **3. Context Management for Database Connections**
```python
import sqlite3

with sqlite3.connect("example.db") as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")
    cursor.execute("INSERT INTO users VALUES (1, 'Alice')")
    conn.commit()  # Automatically commits and closes
```

---

## **4. Creating a Custom Context Manager**
You can define your own context manager using **a class with `__enter__()` and `__exit__()` methods**.

```python
class MyContext:
    def __enter__(self):
        print("Entering context")
        return self  # Return resource (if needed)
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")
        if exc_type:
            print(f"Exception: {exc_value}")  # Handle exceptions if needed
        return True  # Suppresses exception (if needed)

with MyContext():
    print("Inside the context block")
    # raise ValueError("Oops!")  # Uncomment to test exception handling
```

✅ **How it Works:**
- `__enter__()` is called at the start of the `with` block.
- `__exit__()` is called at the end, **even if an exception occurs**.
- `return True` in `__exit__()` suppresses exceptions.

---

## **5. Context Management Using `contextlib`**
Python’s `contextlib` provides a simpler way to create context managers using **generators**.

```python
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Entering context")
    yield "Resource"
    print("Exiting context")

with my_context() as res:
    print(f"Using: {res}")
```

✅ **Easier than defining `__enter__()` and `__exit__()` manually**.

---

## **6. Common Use Cases**
| **Use Case** | **Example** |
|-------------|------------|
| **File Handling** | `with open("file.txt", "r") as f:` |
| **Database Connections** | `with sqlite3.connect("db.db") as conn:` |
| **Locking Resources** | `with threading.Lock():` |
| **Managing Network Connections** | `with socket.create_connection(address) as conn:` |
| **Temporary Files** | `with tempfile.TemporaryFile() as tmpfile:` |

---

### **Final Thoughts**
- ✅ **Use `with` for cleaner, safer resource handling.**
- ✅ **Custom context managers help manage any resource efficiently.**
- ✅ **Use `contextlib` for a simpler approach.**

