### **File Handling in Python**
Python provides built-in functions to work with files—reading, writing, appending, and managing them. 

---

## **1. Opening a File**
The `open()` function is used to open a file in Python.

### **Syntax:**
```python
file = open("filename", "mode")
```
| **Mode** | **Description** |
|---------|----------------|
| `"r"` | Read mode (default) |
| `"w"` | Write mode (overwrites if file exists) |
| `"a"` | Append mode (adds content at the end) |
| `"x"` | Create mode (fails if file exists) |
| `"b"` | Binary mode (use with `r`, `w`, or `a`) |
| `"t"` | Text mode (default) |

---

## **2. Reading from a File**
#### **Reading the entire file**
```python
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()
```

#### **Reading line by line**
```python
file = open("sample.txt", "r")
for line in file:
    print(line.strip())  # Removes newline characters
file.close()
```

#### **Reading a specific number of characters**
```python
file = open("sample.txt", "r")
print(file.read(10))  # Reads first 10 characters
file.close()
```

#### **Using `readlines()` to get a list of lines**
```python
file = open("sample.txt", "r")
lines = file.readlines()  # Returns a list of lines
print(lines)
file.close()
```

---

## **3. Writing to a File**
#### **Overwrite an existing file (`"w" mode`)**
```python
file = open("output.txt", "w")
file.write("This is a new file.\n")
file.write("Overwrites existing content.\n")
file.close()
```
✅ **Warning:** If `output.txt` exists, it will be **erased** before writing.

#### **Appending to a file (`"a" mode`)**
```python
file = open("output.txt", "a")
file.write("This line is added at the end.\n")
file.close()
```

---

## **4. Using `with` Statement (Best Practice)**
Using `with` ensures files are properly closed after use.

```python
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)  # File is automatically closed after this block
```

✅ **Advantage:** No need to manually call `file.close()`.

---

## **5. Working with Binary Files**
Used for **images, videos, PDFs, etc.**

#### **Writing a binary file**
```python
with open("image.jpg", "rb") as file:
    binary_data = file.read()
```

#### **Copying a binary file**
```python
with open("image.jpg", "rb") as source:
    with open("copy.jpg", "wb") as target:
        target.write(source.read())
```

---

## **6. Checking if a File Exists (`os` Module)**
Before reading or deleting a file, check if it exists.

```python
import os

if os.path.exists("sample.txt"):
    print("File exists")
else:
    print("File not found")
```

---

## **7. Deleting a File**
```python
import os

if os.path.exists("output.txt"):
    os.remove("output.txt")
    print("File deleted")
else:
    print("File does not exist")
```

---

## **8. File Handling with Exception Handling**
To avoid errors, use `try-except`.

```python
try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found.")
```

---

## **9. File Pointer Positions**
#### **Get current position**
```python
file = open("sample.txt", "r")
print(file.tell())  # Position in file
file.read(5)        # Read 5 characters
print(file.tell())  # Updated position
file.close()
```

#### **Move file pointer (`seek()`)**
```python
file = open("sample.txt", "r")
file.seek(10)  # Move to 10th byte
print(file.read())  # Read from 10th byte onward
file.close()
```

---

## **10. Summary**
| **Operation** | **Mode** | **Description** |
|--------------|---------|----------------|
| Read | `"r"` | Opens file for reading (file must exist) |
| Write | `"w"` | Opens file for writing (erases existing content) |
| Append | `"a"` | Opens file for appending data |
| Create | `"x"` | Creates a new file (fails if exists) |
| Binary Read | `"rb"` | Opens binary file for reading |
| Binary Write | `"wb"` | Opens binary file for writing |
| Safe File Handling | `with open(...)` | Closes file automatically |

---

Would you like an example of **handling large files**, **CSV files**, or **JSON file operations**? 🚀
