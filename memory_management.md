## Memory Management in Python
Understanding Memory allocation is important to any software developer as writing efficient code means writing a memory-efficient code.
Memory allocation can be defined as allocating a block of space in the computer memory to a program.
In Python memory allocation and deallocation method is automatic as the Python developers created a garbage collector for Python so that the user does not have to do manual 
garbage collection.

## Garbage Collection
Garbage collection is a process in which the interpreter frees up the memory when not in use to make it available for other objects.
Assume a case where no reference is pointing to an object in memory i.e. it is not in use so, 
the virtual machine has a garbage collector that automatically deletes that object from the heap memory.

### Generational Garbage Collection
When attempting to add an object to a reference counter, a cyclical reference or reference cycle is produced. Because the object’s reference counter could never reach 0 (due to cycle), a reference counter cannot destroy the object. Therefore, in situations like this, we employ the universal waste collector. It operates and releases the memory used. A Generational Garbage Collector can be found in the standard library’s gc module.

### Automatic Garbage Collection of Cycles
Because reference cycles take computational work to discover, garbage collection must be a scheduled activity. Python schedules garbage collection based upon a threshold of object allocations and object deallocations. When the number of allocations minus the number of deallocations is greater than the threshold number, the garbage collector is run. One can inspect the threshold for new objects (objects in Python known as generation 0 objects) by importing the gc module and asking for garbage collection thresholds:

```
# loading gc
import gc

# get the current collection 
# thresholds as a tuple
print("Garbage collection thresholds:",
					gc.get_threshold())

#Garbage collection thresholds: (700, 10, 10) 

```


Here, the default threshold on the above system is 700. This means when the number of allocations vs. the number of deallocations is greater than 700 the automatic garbage collector will run. Thus any portion of your code which frees up large blocks of memory is a good candidate for running manual garbage collection. 

### Manual Garbage Collection
Invoking the garbage collector manually during the execution of a program can be a good idea for how to handle memory being consumed by reference cycles. 
The garbage collection can be invoked manually in the following way: 
```
# Importing gc module
import gc

# Returns the number of
# objects it has collected
# and deallocated
collected = gc.collect()

# Prints Garbage collector 
# as 0 object
print("Garbage collector: collected",
		"%d objects." % collected)

```
There are two ways for performing manual garbage collection: time-based and event-based garbage collection. 

1. Time-based garbage collection is simple: the garbage collector is called after a fixed time interval. 
2. Event-based garbage collection calls the garbage collector on event occurrence. For example, when a user exits the application or when the application enters into an idle state.

### Advantages :
1. **Automated memory management:** To avoid memory leaks and lower the chance of running out of memory, the Python garbage collector automatically removes objects that are no longer referenced.
2. **Memory management made easier:** The garbage collector frees developers from having to manually manage memory so they can concentrate on creating code, making Python a higher-level and more practical language for developers.
3. **Efficient memory cleanup:** The garbage collector is designed to minimise performance effects while swiftly identifying and collecting short-lived objects via generational garbage collection.
4. **Customizable settings:** The garbage collector provides options to customize its settings, such as adjusting the thresholds for different generations, allowing developers to fine-tune the garbage collection process based on their specific application requirements.
   
### Disadvantages :
1. **Impact on performance:** Although the garbage collector is designed to efficiently clean up unused memory, there may still be some CPU consumption and execution time overhead, particularly when working with a large number of objects.
2. **The difficulty of memory management:** Although Python’s garbage collector makes managing memory easier, using it successfully may still necessitate knowledge of concepts like object lifetimes, object references, and garbage collection algorithms.
3. **Limited control over memory management:** The autonomous nature of the garbage collector leaves developers with little control over the precise timing and behaviour of memory cleanup, which may not be ideal for many application scenarios where fine-grained control over memory management is necessary.
4. **Bug potential:** Although the garbage collector is intended to be dependable and effective, it is not impervious to errors or atypical behaviour, which could lead to memory leaks or improper object cleanup.

 

Note: For more information, refer to Garbage Collection in Python

## Reference Counting
Reference counting works by counting the number of times an object is referenced by other objects in the system. 
When references to an object are removed, the reference count for an object is decremented. When the reference count becomes zero, the object is deallocated.

For example, Let’s suppose there are two or more variables that have the same value, so, 
what Python virtual machine does is, rather than creating another object of the same value in the private heap, 
it actually makes the second variable point to that originally existing value in the private heap. Therefore, in the case of classes, 
having a number of references may occupy a large amount of space in the memory, 
in such a case referencing counting is highly beneficial to preserve the memory to be available for other objects

```
x = 10
y = x 

if id(x) == id(y): 
	print("x and y refer to the same object") 
```

## There are two parts of memory:

1.stack memory
2. heap memory
The methods/method calls and the references are stored in stack memory and all the values objects are stored in a private heap.

## Work of Stack Memory
The allocation happens on contiguous blocks of memory. We call it stack memory allocation because the allocation happens in the function call stack. 
The size of memory to be allocated is known to the compiler and whenever a function is called, its variables get memory allocated on the stack.

It is the memory that is only needed inside a particular function or method call. 
When a function is called, it is added onto the program’s call stack. 
Any local memory assignments such as variable initializations inside the particular functions are stored temporarily on the function call stack, 
where it is deleted once the function returns, and the call stack moves on to the next task. 
This allocation onto a contiguous block of memory is handled by the compiler using predefined routines, and developers do not need to worry about it.

``` 
def func(): 
		
	# All these variables get memory 
	# allocated on stack 
	a = 20
	b = [] 
	c = "" 

```

## Work of Heap Memory
The memory is allocated during the execution of instructions written by programmers.
Note that the name heap has nothing to do with the heap data structure. 
It is called heap because it is a pile of memory space available to programmers to allocated and de-allocate. 
The variables are needed outside of method or function calls or are shared within multiple functions globally are stored in Heap memory.

Example:
```
# This memory for 10 integers 
# is allocated on heap. 
a = [0]*10

```
