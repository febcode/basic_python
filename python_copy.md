# **Deep Copy vs. Shallow Copy in Python**
In Python, when copying objects like lists, dictionaries, or custom objects, we need to understand **shallow copy** and **deep copy** to avoid unintended modifications.

---

## **1. Assignment (`=`) vs. Copying**
If you assign a list to a new variable using `=`, both variables **point to the same object**.

```python
list1 = [1, 2, 3]
list2 = list1  # No copy, just reference

list2[0] = 100  # Modifies both!
print(list1)  # [100, 2, 3]
print(list2)  # [100, 2, 3]
```
✅ **Issue:** Changing `list2` also changes `list1` because both refer to the same memory location.

---

## **2. Shallow Copy (`copy.copy()`)**
A **shallow copy** creates a new object but **does not copy nested objects**—it just references them.

```python
import copy

list1 = [[1, 2], [3, 4]]
list2 = copy.copy(list1)  # Shallow copy

list2[0][0] = 100  # Changes both!
print(list1)  # [[100, 2], [3, 4]]
print(list2)  # [[100, 2], [3, 4]]
```

✅ **Key point:**  
- `list2` is a new object, but **inner lists are still shared** between `list1` and `list2`.  
- Modifying a nested object **affects both copies**.

---

## **3. Deep Copy (`copy.deepcopy()`)**
A **deep copy** creates a completely independent copy, including all nested objects.

```python
list1 = [[1, 2], [3, 4]]
list2 = copy.deepcopy(list1)  # Deep copy

list2[0][0] = 100  # Only modifies list2
print(list1)  # [[1, 2], [3, 4]]
print(list2)  # [[100, 2], [3, 4]]
```
✅ **Key point:**  
- `list2` is fully independent, and modifying it **does not affect `list1`**.

---

## **4. Shallow vs. Deep Copy in a Dictionary**
```python
dict1 = {"a": [1, 2], "b": [3, 4]}
dict2 = copy.copy(dict1)  # Shallow copy
dict3 = copy.deepcopy(dict1)  # Deep copy

dict2["a"][0] = 100  # Changes both dict1 and dict2!
dict3["a"][0] = 500  # Only changes dict3

print(dict1)  # {'a': [100, 2], 'b': [3, 4]}
print(dict2)  # {'a': [100, 2], 'b': [3, 4]}
print(dict3)  # {'a': [500, 2], 'b': [3, 4]}
```

✅ **Shallow copy shares nested lists, while deep copy fully duplicates the data.**

---

## **5. When to Use Each?**
| **Scenario** | **Use** |
|-------------|--------|
| Simple lists with no nested objects | **Shallow Copy** (`copy.copy()`) |
| Lists, dictionaries, or objects with nested data | **Deep Copy** (`copy.deepcopy()`) |
| When modifying a copy should not affect the original | **Deep Copy** |
| Performance is important and no deep changes are needed | **Shallow Copy** |

---

## **6. Shallow vs. Deep Copy in Custom Objects**
```python
class Person:
    def __init__(self, name, hobbies):
        self.name = name
        self.hobbies = hobbies

p1 = Person("Alice", ["Reading", "Cooking"])
p2 = copy.copy(p1)  # Shallow copy
p3 = copy.deepcopy(p1)  # Deep copy

p2.hobbies.append("Swimming")  # Affects p1 as well!
p3.hobbies.append("Gaming")  # Only affects p3

print(p1.hobbies)  # ['Reading', 'Cooking', 'Swimming']
print(p2.hobbies)  # ['Reading', 'Cooking', 'Swimming']
print(p3.hobbies)  # ['Reading', 'Cooking', 'Gaming']
```

✅ **Shallow copy keeps references, while deep copy duplicates everything.**

---

## **7. Summary**
| **Feature** | **Shallow Copy (`copy.copy()`)** | **Deep Copy (`copy.deepcopy()`)** |
|------------|----------------------------------|----------------------------------|
| Copies top-level object | ✅ Yes | ✅ Yes |
| Copies nested objects | ❌ No (references them) | ✅ Yes (full duplication) |
| Independent from original | ❌ No (changes affect both) | ✅ Yes (completely separate) |
| Performance | ⚡ Faster | 🐢 Slower |

---

## **Final Thoughts**
- ✅ Use **shallow copy** if your data does not have nested structures.  
- ✅ Use **deep copy** when you need a completely independent object.  

Would you like a **real-world example** like handling copies of API responses or database records? 🚀
