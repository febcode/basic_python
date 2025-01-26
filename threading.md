Threading in Python is a way to achieve concurrent execution in a program by running multiple threads within a single process. Threads are smaller units of a process that can run independently, sharing the same memory space. Python provides the threading module to work with threads.

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



