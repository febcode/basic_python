# Python Lambda Functions 
are anonymous functions means that the function is without a name. As we already know the def keyword is used to define a normal function in Python. 
Similarly, the lambda keyword is used to define an anonymous function in Python. 

In the example, we defined a lambda function(upper) to convert a string to its upper case using upper().

```
s1 = 'GeeksforGeeks'

s2 = lambda func: func.upper()
print(s2(s1))

#output
GEEKSFORGEEKS
a= lambda
```

Python Lambda Function Syntax
# Syntax: lambda arguments : expression

**lambda:** The keyword to define the function.
**arguments:** A comma-separated list of input parameters (like in a regular function).
**expression:** A single expression that is evaluated and returned.

Difference Between lambda and def Keyword
lambda is concise but less powerful than def when handling complex logic. Let’s take a look at short comparison between the two:

| Feature	| lambda Function	| Regular Function (def) |
| ----- | -------- | ------------------|
|Definition |	Single expression with lambda.	| Multiple lines of code.|
|Name	 | Anonymous (or named if assigned).	| Must have a name. |
| Statements	| Single expression only. | 	Can include multiple statements.|
| Documentation	| Cannot have a docstring.	|Can include docstrings. |
| Reusability |	Best for short, temporary functions. |	Better for reusable and complex logic.|

# map()
The map() function in Python takes in a function and a list as an argument. 
The function is called with a lambda function and a new list is returned which contains 
all the lambda-modified items returned by that function for each item.
```# Example: 
# Example: Double each number in a list
a = [1, 2, 3, 4]
b = map(lambda x: x * 2, a)
print(list(b))
```
# reduce()
The reduce() function in Python takes in a function and a list as an argument. 
The function is called with a lambda function and an iterable and a new reduced result is returned. 
This performs a repetitive operation over the pairs of the iterable. The reduce() function belongs to the functools module. 

```
from functools import reduce

# Example: Find the product of all numbers in a list
a = [1, 2, 3, 4]
b = reduce(lambda x, y: x * y, a)
print(b)
```

# sorted()
The “key” parameter in Python functions like sorted() or max() allows specifying a function to be used for custom sorting or comparison. 
Lambda functions are often used here to define a key based on which the sorting or comparison is performed.
For example, using sorted() with a lambda function to sort a list of tuples based on the second element:
```
data = [(1, 'apple'), (3, 'orange'), (2, 'banana')]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Output: [(1, 'apple'), (2, 'banana'), (3, 'orange')]

```
