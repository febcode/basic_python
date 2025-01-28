# Lambda function example 
a= lambda x,y:x+y
print(a(5,6))

#output 11 

# Example: Check if a number is positive, negative, or zero
n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

print(n(5))   
print(n(-3))  
print(n(0))