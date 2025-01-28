| **Data Type**| **Classes**      | **Summary**                      |
| :----------- | :--------------: | -------------------------: |
| Numeric      | int              | The int data type holds whole numbers, both positive and negative.  |
|              | float   | The float data type represents real numbers, including decimal points. |
|              | Complex |The complex data type represents complex numbers, consisting of a real part and an imaginary part. |
|Text |str |The str data type is used to store characters, commonly known as strings. |
|Sequence | list | The list data type is used to store ordered collections of items, which can be of different types.|
| |tuple |The tuple data type holds an ordered collection of items, similar to a list, but it is immutable (cannot be modified after creation).|
| |range| The range data type represents a sequence of numbers, typically used in loops for iteration. |
|Boolean| bool | The bool data type is used to represent Boolean values which are either True or False. |
| Set | set | The set data type is used for storing unordered collections of unique items. |
| | frozenset |The ‘frozenset’ data type in Python is used for storing an immutable and unordered collection of unique items.|
|Mapping| dict | The ‘dict’ data type is used to store data values in key:value pairs, forming a mutable and unordered map.|
|None| NoneType |The ‘NoneType’ represents the absence of a value and is denoted by the singleton ‘None’.|


## Primitive data types
Primitive data types are fundamental data types in a programming language that represent simple values. For instance, numbers, strings, etc.
eg .Integers (int) , Floats (float) ,Strings (str) ,Booleans (bool) , NoneType (None)

## Compound data types 
are data types that can hold different types of values together. They are basically composed of other data types, such as lists, for instance.
1. Lists (list)
```
topics_covered = ["Variables", "Loops", "Functions", "Data Structures"]
random_list = [17, 5.5, 17, "This is an element in a list", "Hello!", True, None]
print(random_list)

random_list[0] = 10
print("List after updation:", random_list)
```
2. Tuples (tuple)
```
days_of_the_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
random_tuple = (12, "How is your Python Journey going?", False, True, 25.6, 25.6)
print(random_tuple)

# comment the line below to remove the error as it will give error 
# TypeError: 'tuple' object does not support item assignment
random_tuple[0] = 20
print(random_tuple) 
```
3. Dictionaries (dict)
```
instructors_courses = {"Ash": "Python Basics", "X12": "Advanced Python", "Is": "Data Science / ML with Python"}
random_dict = {"key1": "value1", "key2": 42, "key3": True}
print(random_dict)

random_dict["new_key"] = "Hope you're learning well!"
print("Dictionary after updation:", random_dict)
```
4. Sets (set)
```
set_variable = {1, 2, 3, "How many data types are there?"}
random_set = {1, 2, 3, 4}
print(random_set)

random_set.add(1)
print("Set after updation: ", random_set)
#it will not add ner item 1 in set as it is unique
```

### List vs tuple vs dictionary vs set data types
1) Lists are mutable sequences in Python, meaning they allow for dynamic changes. 
In contrast, tuples are immutable (fixed collections) that can’t be changed. 
Dictionaries store key-value pairs and allow for fast lookups,
while sets are unordered collections of unique elements.

2) In highly simplistic terms, lists are like dynamic containers that you can change,
tuples are fixed containers you can’t change,
dictionaries are similar to labeled boxes used for quick searches,
and sets are like unique bags where each item is different.

## Differences between List and Tuple in Python
|Sno | LIST |TUPLE |
| :----------- | :--------------: | -------------------------: |
|1 |	Lists are mutable |	Tuples are immutable |
|2|	The implication of iterations is Time-consuming	|The implication of iterations is comparatively Faster|
|3 |The list is better for performing operations, such as insertion and deletion. |	A Tuple data type is appropriate for accessing the elements|
|4|Lists consume more memory|	Tuple consumes less memory as compared to the list|
|5|	Lists have several built-in methods|	Tuple does not have many built-in methods.|
|6|	Unexpected changes and errors are more likely to occur|	Because tuples don’t change they are far less error-prone.|

## When to Use Tuples Over Lists?
In Python, tuples and lists are both used to store collections of data, but they have some important differences.
Here are some situations where you might want to use tuples instead of lists – 

**Immutable Data** – Tuples are immutable, thus once they are generated, their contents cannot be changed. 
This makes tuples a suitable option for storing information that shouldn’t change, such as setup settings, constant values,
or other information that should stay the same while your programme is running.

**Performance** – Tuples are more lightweight than lists and might be quicker to generate, access, and iterate through since they are immutable.
Using a tuple can be more effective than using a list if you have a huge collection of data that you need to store, retrieve, 
and use regularly and that data does not need to be altered.

**Data integrity** – By ensuring that the data’s structure and contents stay consistent, 
tuples can be utilised to ensure data integrity. 
To make sure the caller is aware of how much data to expect, for instance, if a function returns a set amount of values, 
you might want to return them as a tuple rather than a list.

#### In Python, set and frozenset are both data structures used to store collections of unique elements. Here's a breakdown of their key differences:
### Set:
**Mutable:** You can add or remove elements from a set after its creation.
**Unordered:** Elements are not stored in any specific order.
**Unhashable:** A set cannot be used as a key in a dictionary because it is mutable.
### Frozenset:
**Immutable:** Once created, you cannot modify its elements.
**Unordered:** Similar to sets, elements are not stored in any specific order.
**Hashable:** A frozenset can be used as a key in a dictionary because it is immutable.

### Common Use Cases:
**Set:** Used when you need to store a collection of unique elements and might need to modify it later.
**Frozenset:** Used when you need an immutable set, for example:
  As a key in a dictionary
  As an element in another set

