# **Pickling and Unpickling in Python** 🥒

Pickling and unpickling are used to **serialize and deserialize** Python objects, allowing you to save them to a file or send them over a network.

---

## **1. What is Pickling?**
Pickling converts a Python object into a **byte stream** (serialization) so that it can be stored in a file or sent over a network.

## **2. What is Unpickling?**
Unpickling is the **reverse process**—it converts the byte stream back into a Python object (deserialization).

---

## **3. Pickling Example**
```python
import pickle

data = {"name": "Alice", "age": 25, "city": "New York"}

# Open a file in write-binary mode
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)  # Serialize (Pickle)
    
print("Data pickled successfully!")
```
✅ Saves `data.pkl` containing the serialized dictionary.

---

## **4. Unpickling Example**
```python
with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)  # Deserialize (Unpickle)

print(loaded_data)  # {'name': 'Alice', 'age': 25, 'city': 'New York'}
```
✅ Successfully retrieves the original Python dictionary.

---

## **5. Pickling and Unpickling a Custom Object**
You can pickle custom classes and objects.

### **Pickling a Class Object**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 25)

with open("person.pkl", "wb") as file:
    pickle.dump(person, file)  # Serialize
```

### **Unpickling the Object**
```python
with open("person.pkl", "rb") as file:
    loaded_person = pickle.load(file)  # Deserialize

print(loaded_person.name, loaded_person.age)  # Alice 25
```
✅ The object is successfully restored.

---

## **6. When to Use Pickling?**
| **Use Case** | **Why?** |
|-------------|---------|
| **Save program state** | Store Python objects and reload them later |
| **Send objects over a network** | Transfer data between processes |
| **Caching** | Store processed data to avoid recomputation |

---

## **7. Important Notes**
❌ **Security Warning:** Never unpickle data from untrusted sources (it may execute malicious code).  
✅ **Alternative:** Use JSON for simple data types (dict, list, str, int).  

```python
import json

data = {"name": "Alice", "age": 25}
json_string = json.dumps(data)  # Serialize
data = json.loads(json_string)  # Deserialize
```
✅ **JSON is safer** and works across different languages.

---

## **Final Thoughts**
- ✅ **Pickle for complex Python objects** (classes, lists, dictionaries).  
- ✅ **Use JSON for safer, human-readable data exchange**.  
- ❌ **Do NOT unpickle data from untrusted sources** (security risk).  

