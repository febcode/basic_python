### **`range` vs `xrange` in Python** 🚀

In **Python 2**, both `range()` and `xrange()` exist, but in **Python 3**, `xrange()` was **removed**, and `range()` behaves like `xrange()` from Python 2.

---

## **1. `range()` in Python 3**
- `range()` **returns an iterator** (like `xrange` in Python 2).  
- It does **not create a list in memory** but generates values on demand.  
- It's memory efficient and supports iteration in loops.

### **Example: Using `range()` in Python 3**
```python
for num in range(1, 5):  
    print(num)
```
**Output:**
```
1
2
3
4
```
✅ `range()` **generates numbers one by one** instead of storing them all in memory.

---

## **2. `range()` vs `xrange()` in Python 2**
| Feature | `range()` (Python 2 & 3) | `xrange()` (Python 2 only) |
|---------|----------------|------------------|
| **Returns** | List (Python 2), Iterator (Python 3) | Iterator |
| **Memory Usage** | High (Python 2), Efficient (Python 3) | Efficient |
| **Supports Slicing?** | ✅ Yes (Python 2), ❌ No (Python 3) | ❌ No |
| **Supports `len()`?** | ✅ Yes | ❌ No |

### **Example in Python 2**
```python
print(range(1, 5))   # [1, 2, 3, 4] (List)
print(xrange(1, 5))  # xrange(1, 5) (Iterator)
```

---

## **3. Why was `xrange()` Removed in Python 3?**
- Python 3's `range()` is **optimized** like `xrange()` in Python 2.
- **No need for two functions**—`range()` is now memory-efficient.

### **Example: Large Range in Python 3**
```python
nums = range(10**6)  # Uses almost no memory!
print(type(nums))  # <class 'range'>
```
✅ Unlike Python 2, `range(10**6)` **does not create a list** in Python 3.

---

## **4. When to Use `range()`?**
- Use `range(start, stop, step)` for **loops**.
- Use `list(range(n))` if you **really need a list**.

### **Custom `range()` Function in Python** 🚀  

Python’s built-in `range()` is powerful, but sometimes, you may need a **custom range function** with added features. Below are some custom implementations.

---

## **1. Simple Custom `my_range()` Function**  
Let's implement a basic version of `range()` using a generator.

### **Example:**
```python
def my_range(start, stop, step=1):
    while start < stop:
        yield start
        start += step

for num in my_range(1, 5):
    print(num)
```
**Output:**
```
1
2
3
4
```
✅ **Generates numbers dynamically** (memory efficient).

---

## **2. Supporting Negative Steps**
This version supports **both increasing and decreasing sequences**.

### **Example:**
```python
def my_range(start, stop, step=1):
    if step == 0:
        raise ValueError("Step cannot be zero!")
    if (step > 0 and start >= stop) or (step < 0 and start <= stop):
        return  # Stop immediately if the range is invalid

    while (step > 0 and start < stop) or (step < 0 and start > stop):
        yield start
        start += step

print(list(my_range(5, 1, -1)))  # [5, 4, 3, 2]
```
**Output:**
```
[5, 4, 3, 2]
```
✅ Handles both **positive and negative steps**.

---

## **3. Infinite Range (Like `itertools.count()`)**  
This **infinite generator** continues indefinitely.

### **Example:**
```python
def infinite_range(start=0, step=1):
    while True:
        yield start
        start += step

# Be careful! This loop runs forever.
for num in infinite_range(10, 5):
    print(num)
    if num > 30:
        break  # Stop manually
```
**Output:**
```
10
15
20
25
30
35
```
✅ **Useful for infinite loops** like reading a live data stream.

---

## **4. Custom Float Range (`frange()`)**  
Python’s built-in `range()` **doesn’t support floats**. Let’s create a version that does.

### **Example:**
```python
def frange(start, stop, step=0.1):
    while start < stop:
        yield round(start, 10)  # Avoid floating-point precision errors
        start += step

print(list(frange(1.0, 2.0, 0.2)))
```
**Output:**
```
[1.0, 1.2, 1.4, 1.6, 1.8]
```
✅ Generates **decimal step ranges**.

---

## **5. Range with a Specific Number of Steps (`n_range()`)**
Instead of a fixed step size, we define **N total steps**.

### **Example:**
```python
def n_range(start, stop, num_steps):
    step = (stop - start) / (num_steps - 1)
    for _ in range(num_steps):
        yield round(start, 10)
        start += step

print(list(n_range(1, 5, 4)))  # 4 steps from 1 to 5
```
**Output:**
```
[1.0, 2.3333333333, 3.6666666667, 5.0]
```
✅ Useful for **evenly spaced points**, such as plotting.

---

## **Summary**
| **Custom Range Function** | **Feature** |
|--------------------------|-------------|
| `my_range()` | Basic range generator |
| `my_range()` (Enhanced) | Supports negative steps |
| `infinite_range()` | Infinite sequence generator |
| `frange()` | Floating-point range |
| `n_range()` | Fixed number of steps |

