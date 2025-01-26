# Threading
 in Python is a way to achieve concurrent execution in a program by running multiple threads within a single process. Threads are smaller units of a process that can run independently, sharing the same memory space. Python provides the threading module to work with threads.

## Key Concepts:

1. **Thread:** A sequence of instructions that can execute independently.


2. **Concurrency: ** Multiple threads running seemingly at the same time. Note: Python's threading is limited by the Global Interpreter Lock (GIL), which allows only one thread to execute Python bytecode at a time.




---

## Why Use Threading?

To perform I/O-bound tasks (e.g., reading/writing files, network requests).

To improve the responsiveness of applications, especially GUIs, where a long-running task can block the main thread.



---
'''
Example of Threading:

import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

# Creating threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)

# Starting threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("Threads completed.")

Output (may vary due to concurrency):

Number: 0
Number: 0
Number: 1
Number: 1
Number: 2
Number: 2
...
Threads completed.
'''


---

Key Methods in the threading Module:

1. Thread:

start(): Starts a thread's execution.

join(): Waits for the thread to finish execution.

is_alive(): Checks if the thread is still running.



2. Lock and Synchronization:

Prevents race conditions where multiple threads access shared data simultaneously.


lock = threading.Lock()
lock.acquire()
# Critical section
lock.release()


3. Daemon Threads:

Use daemon=True when creating a thread to make it a background thread, which exits when the main program exits.





---

Limitations of Threading:

Global Interpreter Lock (GIL):

Only one thread executes Python bytecode at a time, which limits the performance of CPU-bound tasks in multi-threaded programs.

For CPU-bound tasks, consider using multiprocessing.



When to Use:

Use threading for I/O-bound tasks.

Use multiprocessing for CPU-bound tasks.




# Thread-Safe Code Example with Locks

When multiple threads access shared resources (like a variable or a data structure), it can lead to race conditions, where the threads interfere with each other, causing unexpected behavior. To prevent this, locks are used to ensure only one thread accesses the critical section at a time.

Here’s an example of thread-safe code using threading.Lock:


---

Example: Incrementing a Shared Variable Safely

'''
import threading

# Shared resource
counter = 0

# Lock to ensure thread safety
lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(100000):
        # Critical section
        lock.acquire()
        counter += 1
        lock.release()

# Creating threads
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)

# Starting threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()

print(f"Final counter value: {counter}")

'''
---

Output:

Final counter value: 200000

Without the lock, the output might vary (e.g., 199999), as multiple threads might access and update counter simultaneously, causing a race condition.


---

Explanation of the Code:

1. lock.acquire(): A thread acquires the lock before entering the critical section.


2. Critical Section: The part of the code that modifies the shared resource (counter).


3. lock.release(): The lock is released after the modification, allowing other threads to proceed.




---

# Global Interpreter Lock (GIL) in Python

The GIL is a mechanism in CPython (the standard Python implementation) to ensure that only one thread executes Python bytecode at a time. This simplifies memory management but limits true parallelism for CPU-bound tasks.

How It Affects Threading:

I/O-bound tasks (e.g., network calls, file operations): Threading works well because threads can release the GIL while waiting for I/O.

CPU-bound tasks (e.g., complex computations): The GIL limits performance since only one thread can execute Python bytecode at a time.


Example Showing GIL Limitation:
'''
import threading
import time

def cpu_bound_task():
    start = time.time()
    for _ in range(10**7):
        pass
    print(f"Task done in {time.time() - start} seconds.")

# Creating multiple threads
thread1 = threading.Thread(target=cpu_bound_task)
thread2 = threading.Thread(target=cpu_bound_task)

start = time.time()
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(f"Total time: {time.time() - start} seconds.")

Output (simulated example):
'''

Expected time without GIL: Less than twice the time of a single thread.

Actual time due to GIL: Almost twice the time of a single thread because threads run sequentially for Python bytecode.



---

Overcoming GIL for CPU-Bound Tasks:

# Multiprocessing:

Use the multiprocessing module, which creates separate processes instead of threads.

Each process has its own memory space and GIL, enabling true parallelism.


from multiprocessing import Process

def cpu_task():
    for _ in range(10**7):
        pass

p1 = Process(target=cpu_task)
p2 = Process(target=cpu_task)

p1.start()
p2.start()

p1.join()
p2.join()
print("Processes completed.")


2. Cython or JIT Compilers:

Use Cython or tools like PyPy, which can eliminate or bypass the GIL for performance-critical code.

---

# Async Programming in Python

For I/O-bound tasks where threads or processes might still involve unnecessary overhead, async programming can handle thousands of tasks efficiently using a single thread.

Asyncio: Event-Driven Programming

Python's asyncio library allows you to handle multiple asynchronous tasks without threads or processes.

Example: Async Web Requests
'''
import asyncio
import time

async def fetch_data(n):
    print(f"Task {n}: Fetching data...")
    await asyncio.sleep(2)  # Simulate I/O delay
    print(f"Task {n}: Data fetched.")
    return n

async def main():
    tasks = [fetch_data(i) for i in range(5)]
    results = await asyncio.gather(*tasks)
    print(f"Results: {results}")

start = time.time()
asyncio.run(main())
print(f"Total time: {time.time() - start:.2f} seconds.")

Output:

Task 0: Fetching data...
Task 1: Fetching data...
Task 2: Fetching data...
Task 3: Fetching data...
Task 4: Fetching data...
Task 0: Data fetched.
Task 1: Data fetched.
...
Results: [0, 1, 2, 3, 4]
Total time: 2.00 seconds.

'''
---

When to Use Each Approach



