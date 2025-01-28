# Lambda function example 
a= lambda x,y:x+y
print(a(5,6))

#output 11 

# Example: Check if a number is positive, negative, or zero
n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

print(n(5))   
print(n(-3))  
print(n(0))

# Using lambda
sq = lambda x: x ** 2
print(sq(3))

# Using def
def sqdef(x):
    return x ** 2
print(sqdef(3))

# Lambda with List Comprehension

li = [lambda arg=x: arg * 10 for x in range(1, 5)] 
print(li)
for i in li:
    print(i())
    
    
# Example: Check if a number is even or odd
check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(4))  
print(check(7))

# Example: Perform addition and multiplication in a single line
calc = lambda x, y: (x + y, x * y)

res = calc(3, 4)
print(res)

# The map() function in Python takes in a function and a list as an argument. 
# The function is called with a lambda function and a new list is returned which contains 
# all the lambda-modified items returned by that function for each item.
# Example: 
# Example: Double each number in a list
a = [1, 2, 3, 4]
b = map(lambda x: x * 2, a)
print(list(b))

# reduce()
# The reduce() function in Python takes in a function and a list as an argument. 
# The function is called with a lambda function and an iterable and a new reduced result is returned. 
# This performs a repetitive operation over the pairs of the iterable. The reduce() function belongs to the functools module. 

from functools import reduce

# Example: Find the product of all numbers in a list
a = [1, 2, 3, 4]
b = reduce(lambda x, y: x * y, a)
print(b)


# # sorted()
# The “key” parameter in Python functions like sorted() or max() allows specifying a function to be used for custom sorting or comparison. 
# Lambda functions are often used here to define a key based on which the sorting or comparison is performed.
# For example, using sorted() with a lambda function to sort a list of tuples based on the second element:

data = [(1, 'apple'), (3, 'orange'), (2, 'banana')]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Output: [(1, 'apple'), (3, 'banana'), (2, 'orange')]

d = [[1,10],[2,40],[3,90],[4,70],[5,90]]
listn = sorted(d,key = lambda i:i[1])
print(listn)
