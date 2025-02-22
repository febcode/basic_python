# **Iterators in Python** 🔄  

An **iterator** in Python is an object that can be iterated (looped) over, returning elements **one at a time**.

---

## **1. What is an Iterator?**
An **iterator** is an object that:
1. Implements the `__iter__()` method (returns the iterator itself).
2. Implements the `__next__()` method (returns the next item).

### **Example: Manually Using an Iterator**
```python
numbers = [1, 2, 3]
iterator = iter(numbers)  # Get an iterator object

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
# print(next(iterator))  # ❌ Raises StopIteration (end of iteration)
```
**Output:**
```
1
2
3
```
✅ Each `next(iterator)` call retrieves the next element until it **raises `StopIteration`**.

---

## **2. Creating a Custom Iterator**
You can create a **custom iterator** by defining a class with `__iter__()` and `__next__()` methods.

### **Example: Custom Iterator for Counting**
```python
class CountUp:
    def __init__(self, max_value):
        self.max = max_value
        self.current = 0

    def __iter__(self):
        return self  # An iterator should return itself

    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration  # End of iteration

counter = CountUp(5)
for num in counter:
    print(num)
```
**Output:**
```
1
2
3
4
5
```
✅ **Each iteration calls `__next__()` until `StopIteration` is raised.**

---

## **3. Using `iter()` with a Sentinel Value**
The `iter()` function can take two arguments: **a function and a sentinel value**.

### **Example: Read Input Until "STOP"**
```python
def get_input():
    return input("Enter something (type STOP to end): ")

for value in iter(get_input, "STOP"):
    print(f"You entered: {value}")
```
✅ The loop runs **until "STOP" is entered**.

---

## **4. Iterators vs Iterables**
| Feature | **Iterator** | **Iterable** |
|---------|------------|------------|
| **Definition** | Implements `__iter__()` and `__next__()` | Implements `__iter__()`, returns an iterator |
| **Stateful?** | ✅ Yes (tracks position) | ❌ No (returns a new iterator) |
| **Example** | `iter([1,2,3])` | `[1,2,3]` (list, tuple, set, etc.) |

### **Example: Iterable vs Iterator**
```python
numbers = [1, 2, 3]  # Iterable
iterator = iter(numbers)  # Iterator

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
# print(next(iterator))  # ❌ StopIteration
```

---

## **5. Generators: A Simpler Alternative to Iterators**
Generators are **iterators**, but easier to create using `yield`.

### **Example: Generator for Counting**
```python
def count_up(max_value):
    current = 1
    while current <= max_value:
        yield current
        current += 1

for num in count_up(5):
    print(num)
```
**Output:**
```
1
2
3
4
5
```
✅ **Generators are memory-efficient** and require less code than a class-based iterator.

---

## **6. Real-World Use Cases**
| **Use Case** | **Why Use an Iterator?** |
|-------------|----------------|
| **Large Data Processing** | Process data one piece at a time without loading everything into memory |
| **Streaming Data** | Read log files, network data, or sensor data efficiently |
| **Lazy Evaluation** | Avoid unnecessary computations until needed |

