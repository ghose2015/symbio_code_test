# Review 1
def add_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list


"""
Something wrong in code
It not judge the input is a list
"""


def add_to_list_revise(value, my_list=[]):
    if isinstance(my_list, list):
        my_list.append(value)
        return my_list
    else:
        return


# Review 2
def format_greeting(name, age):
    return "Hello, my name is {name} and I am {age} years old."

"""
Cannot output name and age
"""

def format_greeting_revise(name, age):
    return f"Hello, my name is {name} and I am {age} years old."


# Review 3
class Counter:
    count = 0

    def __init__(self):
        self.count += 1

    def get_count(self):
        return self.count

"""
ok
"""


# Review 4
import threading


class SafeCounter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


def worker(counter):
    for _ in range(1000):
        counter.increment()


counter = SafeCounter()
threads = []
for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

"""
there is no threading lock
"""

import threading, time
from random import randint


class SafeCounter:
    def __init__(self):
        self.lock = threading.Lock()
        self.count = 0

    def increment(self):
        self.lock.acquire()
        self.count += 1
        self.lock.release()


def worker(counter):
    for _ in range(1000):
        counter.increment()


counter = SafeCounter()
threads = []
for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))

    t.start()
    threads.append(t)

for t in threads:
    t.join()



# Review 5
def count_occurrences(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] = + 1
        else:
            counts[item] = 1
    return counts

"""
list, tuple and dic cannot be used as dic keys
"""


# Review 5
def count_occurrences_revise(lst):
    counts = {}
    for item in lst:
        if isinstance(item, int) or isinstance(item, str) or isinstance(item, float):
            pass
        else:
            item = str(item)
        if item in counts:
            counts[item] = + 1
        else:
            counts[item] = 1
    return counts

