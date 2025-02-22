# **List, Dictionary, and Set Comprehensions in Python** 🚀

Python comprehensions provide a concise way to create **lists, dictionaries, and sets** in a single line.

---

## **1. List Comprehension**
List comprehension is used to create a **new list** from an existing iterable.

### **Basic Syntax:**
```python
new_list = [expression for item in iterable if condition]
```

### **Example 1: Create a List of Squares**
```python
squares = [x**2 for x in range(5)]
print(squares)  
```
**Output:**
```
[0, 1, 4, 9, 16]
```

### **Example 2: Filter Even Numbers**
```python
evens = [x for x in range(10) if x % 2 == 0]
print(evens)
```
**Output:**
```
[0, 2, 4, 6, 8]
```

---

## **2. Dictionary Comprehension**
Dictionary comprehension creates a new dictionary from an iterable.

### **Basic Syntax:**
```python
new_dict = {key_expression: value_expression for item in iterable if condition}
```

### **Example: Create a Dictionary of Squares**
```python
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)
```
**Output:**
```
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### **Example: Swap Keys and Values**
```python
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(swapped)
```
**Output:**
```
{1: 'a', 2: 'b', 3: 'c'}
```

---

## **3. Set Comprehension**
Set comprehension creates a **set** with unique elements.

### **Basic Syntax:**
```python
new_set = {expression for item in iterable if condition}
```

### **Example: Unique Even Numbers**
```python
evens_set = {x for x in range(10) if x % 2 == 0}
print(evens_set)
```
**Output:**
```
{0, 2, 4, 6, 8}
```

---

## **4. Nested Comprehension**
You can use comprehensions inside another comprehension.

### **Example: Nested List Comprehension**
```python
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)
```
**Output:**
```
[[0, 1, 2], [0, 1, 2], [0, 1, 2]]
```

---

## **5. Generator Comprehension**
If you use `()` instead of `[]`, it creates a **generator**, which is memory efficient.

```python
gen = (x**2 for x in range(5))
print(list(gen))  # Convert generator to a list
```
**Output:**
```
[0, 1, 4, 9, 16]
```

---

## **Summary**
| **Comprehension Type** | **Syntax Example** | **Output** |
|----------------|------------------------------|-----------|
| **List** | `[x**2 for x in range(5)]` | `[0, 1, 4, 9, 16]` |
| **Dictionary** | `{x: x**2 for x in range(5)}` | `{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}` |
| **Set** | `{x for x in range(5)}` | `{0, 1, 2, 3, 4}` |
| **Generator** | `(x**2 for x in range(5))` | `generator object` |

