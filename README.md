Live URL:  https://aminbiography.github.io/python-automation-cti/

---      
    
# Essential Python Concepts with Examples and Outputs

## Python Basics      
``` 
print, input, variables, if-else, loops, functions, lists, dictionaries, import, try-except
```
 
---
 
## 1) Setting Up Python

Install Python from the official site: `https://www.python.org/downloads/`

Verify in terminal:

```bash
python --version
# or
python3 --version
```

**Expected output (example):**

```text
Python 3.12.7
```

---

## 2) Hello World

```python
print("Hello, World!")
```

**Output:**

```text
Hello, World!
```

---

## 3) Variables and Data Types

```python
my_variable = 10
my_string = "Hello, Python!"
my_float = 10.5
my_boolean = True

print(my_variable)
print(my_string)
print(my_float)
print(my_boolean)
```

**Output:**

```text
10
Hello, Python!
10.5
True
```

---

## 4) Basic Math Operations

```python
addition = 5 + 3
subtraction = 10 - 4
multiplication = 7 * 3
division = 12 / 4

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
```

**Output:**

```text
Addition: 8
Subtraction: 6
Multiplication: 21
Division: 3.0
```

---

## 5) Lists

```python
my_list = [1, 2, 3, "Python", 5.5]

print(my_list[0])
print(my_list[-1])

my_list.append(100)
print(my_list)
```

**Output:**

```text
1
5.5
[1, 2, 3, 'Python', 5.5, 100]
```

---

## 6) If-Else

```python
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

**Output:**

```text
You are an adult.
```

---

## 7) Loops

### For loop

```python
for i in range(5):
    print("Iteration:", i)
```

**Output:**

```text
Iteration: 0
Iteration: 1
Iteration: 2
Iteration: 3
Iteration: 4
```

### While loop

```python
counter = 0
while counter < 5:
    print("Counter:", counter)
    counter += 1
```

**Output:**

```text
Counter: 0
Counter: 1
Counter: 2
Counter: 3
Counter: 4
```

---

## 8) Functions

```python
def greet(name):
    print("Hello, " + name)

greet("Alice")
greet("Bob")
```

**Output:**

```text
Hello, Alice
Hello, Bob
```

---

## 9) Dictionaries

```python
my_dict = {
    "name": "John",
    "age": 25,
    "location": "New York"
}

print(my_dict["name"])
print(my_dict["age"])

my_dict["age"] = 26
my_dict["job"] = "Engineer"
print(my_dict)
```

**Output:**

```text
John
25
{'name': 'John', 'age': 26, 'location': 'New York', 'job': 'Engineer'}
```

---

## 10) Classes and Objects

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old.")

person1 = Person("Alice", 30)
person1.greet()
```

**Output:**

```text
Hello, my name is Alice and I am 30 years old.
```

---

## 11) Exception Handling (ZeroDivisionError)

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

**Output:**

```text
Cannot divide by zero!
```

---

## 12) File Handling (Write + Read)

```python
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

**Output:**

```text
Hello, this is a test file.
```

---

## 13) Lambda Functions

```python
multiply = lambda x, y: x * y
print(multiply(3, 4))
```

**Output:**

```text
12
```

---

## 14) List Comprehensions

```python
squares = [x**2 for x in range(5)]
print(squares)
```

**Output:**

```text
[0, 1, 4, 9, 16]
```

---

## 15) Modules and Packages (math)

```python
import math

print(math.sqrt(16))
print(math.pi)
```

**Output:**

```text
4.0
3.141592653589793
```

---

## 16) Dates and Times (datetime)

```python
from datetime import datetime

now = datetime.now()
print(now)

formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)
```

**Output (varies by time):**

```text
2025-12-15 07:16:35.123456
2025-12-15 07:16:35
```

---

## 17) Regular Expressions (Find digits)

```python
import re

pattern = r"\d+"
text = "There are 100 apples."
match = re.search(pattern, text)
if match:
    print("Match found:", match.group())
```

**Output:**

```text
Match found: 100
```

---

## 18) Iterators and Generators

### Iterator

```python
my_list = [1, 2, 3, 4]
my_iterator = iter(my_list)

print(next(my_iterator))
print(next(my_iterator))
```

**Output:**

```text
1
2
```

### Generator

```python
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
for value in gen:
    print(value)
```

**Output:**

```text
1
2
3
```

---

## 19) Decorators

```python
def decorator_function(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

@decorator_function
def say_hello():
    print("Hello!")

say_hello()
```

**Output:**

```text
Before the function is called.
Hello!
After the function is called.
```

---

## 20) Working with APIs (requests)

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response.status_code)
print(response.json())
```

**Output (status code is typically stable; JSON may be large):**

```text
200
[{'userId': 1, 'id': 1, 'title': '...', 'body': '...'}, ...]
```

---

## 21) Multithreading (threading)

```python
import threading

def print_numbers():
    for i in range(5):
        print(i)

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)

thread1.start()
thread2.start()
```

**Output (order may vary due to scheduling):**

```text
0
1
2
3
4
0
1
2
3
4
```

---

## 22) Web Development with Flask

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

**Output (sample terminal logs; varies):**

```text
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000/
```

When you visit `/` in the browser, you will see:

```text
Hello, Flask!
```

---

## 23) SQLite Database (sqlite3)

```python
import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)''')

cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
cursor.execute("INSERT INTO users (name) VALUES ('Bob')")
conn.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

conn.close()
```

**Output (first run):**

```text
[(1, 'Alice'), (2, 'Bob')]
```

Note: If you run multiple times without clearing the table, IDs will continue increasing and rows will duplicate.

---

## 24) Unit Testing (unittest)

```python
import unittest

def add(a, b):
    return a + b

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
```

**Output (sample):**

```text
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

---

## 25) Virtual Environments (venv)

Create:

```bash
python -m venv myenv
```

Activate (Windows):

```bash
myenv\Scripts\activate
```

Activate (Mac/Linux):

```bash
source myenv/bin/activate
```

**Output:** Typically no output; your shell prompt changes to show the environment name.

---

## 26) Python Packages (pip + requests)

Install:

```bash
pip install requests
```

Use:

```python
import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response.status_code)
```

**Output:**

```text
200
```

---

## 27) Working with JSON (json)

```python
import json

data = {"name": "Alice", "age": 25}
json_data = json.dumps(data)
print(json_data)

python_data = json.loads(json_data)
print(python_data)
```

**Output:**

```text
{"name": "Alice", "age": 25}
{'name': 'Alice', 'age': 25}
```

---

## 28) File Handling (Write + Read + Append)

```python
with open("sample.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("This is a sample file.")

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

with open("sample.txt", "a") as file:
    file.write("\nAppended content.")
```

**Output (from the read step):**

```text
Hello, Python!
This is a sample file.
```

---

## 29) Sorting and Filtering

```python
numbers = [4, 1, 3, 2, 5]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))
```

**Output:**

```text
[1, 2, 3, 4, 5]
[4, 2]
```

---

## 30) map()

```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))
```

**Output:**

```text
[1, 4, 9, 16, 25]
```

---

## 31) Global and Local Variables

```python
x = 10

def foo():
    global x
    x = 20
    print(x)

foo()
print(x)
```

**Output:**

```text
20
20
```

---

## 32) Recursion (Factorial)

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
```

**Output:**

```text
120
```

---

## 33) reduce()

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total)
```

**Output:**

```text
15
```

---

## 34) Handling Exceptions with input()

```python
try:
    value = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter a valid number.")
else:
    print(f"You entered: {value}")
finally:
    print("This will always be executed.")
```

**Output (example when input is `12`):**

```text
Enter a number: 12
You entered: 12
This will always be executed.
```

**Output (example when input is `abc`):**

```text
Enter a number: abc
Invalid input! Please enter a valid number.
This will always be executed.
```

---

## 35) Working with JSON Files

```python
import json

data = {"name": "Alice", "age": 25}
with open("data.json", "w") as json_file:
    json.dump(data, json_file)

with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)
    print(loaded_data)
```

**Output:**

```text
{'name': 'Alice', 'age': 25}
```

---

## 36) Decorators with Arguments

```python
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
```

**Output:**

```text
Hello!
Hello!
Hello!
```

---

## 37) os module (Directories)

```python
import os

print(os.getcwd())
print(os.listdir("."))

os.mkdir("new_directory")
```

**Output (first two lines vary by system):**

```text
C:\Users\YourName\Projects
['file1.py', 'sample.txt', 'example.db', ...]
```

**Note:** `os.mkdir("new_directory")` creates a folder. If it already exists, Python raises `FileExistsError`.

---

## 38) sys module

```python
import sys

print(sys.argv)
sys.exit("Exiting the program.")
```

**Output (example):**

```text
['script.py']
Exiting the program.
```

Note: `sys.exit(...)` terminates the program immediately after printing the message.

---

## 39) time module

```python
import time

print("Start")
time.sleep(2)
print("End")

start_time = time.time()
for _ in range(1000000):
    pass
end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")
```

**Output (timing varies):**

```text
Start
End
Execution time: 0.03 seconds
```

---

## 40) collections.Counter

```python
from collections import Counter

word_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
word_count = Counter(word_list)
print(word_count)
```

**Output:**

```text
Counter({'apple': 3, 'banana': 2, 'orange': 1})
```

---

## 41) OOP Example (Car)

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"Car Brand: {self.brand}, Model: {self.model}")

my_car = Car("Toyota", "Corolla")
my_car.display()
```

**Output:**

```text
Car Brand: Toyota, Model: Corolla
```

---

## 42) Static Methods and Class Methods

```python
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method.")
    
    @classmethod
    def class_method(cls):
        print("This is a class method.")

MyClass.static_method()
MyClass.class_method()
```

**Output:**

```text
This is a static method.
This is a class method.
```

---

## 43) Context Manager (with open)

```python
with open("example.txt", "w") as file:
    file.write("Hello, Python with context manager!")
```

**Output:** None (it writes to a file).

---

## 44) shutil (Copy + Move)

```python
import shutil

shutil.copy("source.txt", "destination.txt")
shutil.move("source.txt", "new_directory/source.txt")
```

**Output:** None (file operations).
**Note:** This requires `source.txt` to exist and `new_directory` to exist.

---

## 45) sqlite3 (Alternative Example)

```python
import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)''')
cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
connection.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

connection.close()
```

**Output (first run):**

```text
[(1, 'Alice')]
```

---

## 46) Regex (Find exactly 5-letter words)

```python
import re

text = "The quick brown fox jumps over the lazy dog."
pattern = r"\b\w{5}\b"

matches = re.findall(pattern, text)
print(matches)
```

**Output:**

```text
['quick', 'brown', 'jumps']
```

---

## 47) Lambda (Repeat)

```python
multiply = lambda x, y: x * y
print(multiply(3, 4))
```

**Output:**

```text
12
```

---

## 48) itertools.combinations

```python
import itertools

numbers = [1, 2, 3, 4]
combinations = itertools.combinations(numbers, 2)
print(list(combinations))
```

**Output:**

```text
[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
```

---

## 49) Stacks and Queues

```python
stack = []
stack.append(1)
stack.append(2)
print(stack.pop())

from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
print(queue.popleft())
```

**Output:**

```text
2
1
```

---

## 50) socket module (Client/Server)

Your server code includes `accept()` which **blocks until a client connects**.

**Server output (sample):**

```text
Server is waiting for a connection...
Client connected: ('127.0.0.1', 54321)
```

**Client output:** Typically none unless you print something.
**Note:** Networking examples can fail due to port conflicts, firewall rules, or missing server/client coordination.

---

## 51) CSV Files

```python
import csv

header = ["Name", "Age", "Country"]
rows = [["Alice", 25, "USA"], ["Bob", 30, "Canada"]]

with open("people.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)

with open("people.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

**Output:**

```text
['Name', 'Age', 'Country']
['Alice', '25', 'USA']
['Bob', '30', 'Canada']
```

---

## 52) MySQL Example (mysql.connector)

```python
import mysql.connector

connection = mysql.connector.connect(
    host="localhost", user="root", password="password", database="test_db"
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM users")
result = cursor.fetchall()
print(result)

cursor.close()
connection.close()
```

**Output:** Depends on your database contents, e.g.

```text
[(1, 'Alice'), (2, 'Bob')]
```

**Note:** This requires a running MySQL server and correct credentials.

---

## 53) pandas (DataFrame + CSV)

```python
import pandas as pd

data = {"Name": ["Alice", "Bob"], "Age": [25, 30], "Country": ["USA", "Canada"]}
df = pd.DataFrame(data)
print(df)

df2 = pd.read_csv("people.csv")
print(df2)
```

**Output (DataFrame display formatting can vary):**

```text
    Name  Age Country
0  Alice   25     USA
1    Bob   30  Canada

    Name  Age Country
0  Alice   25     USA
1    Bob   30  Canada
```

---

## 54) matplotlib and seaborn (Charts)

Plotting code usually **opens a window** (or renders inline in notebooks). It does not print a standard text output.

**Result:** A line chart and a bar chart are displayed.

---

## 55) numpy

```python
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)

arr2 = np.array([5, 6, 7, 8])
sum_arr = np.add(arr, arr2)
print(sum_arr)
```

**Output:**

```text
[1 2 3 4]
[ 6  8 10 12]
```

---

## 56) Flask (Repeat)

Same behavior as section 22.

---

## 57) Django View (Example)

```python
from django.http import HttpResponse

def my_view(request):
    return HttpResponse("Hello, Django!")
```

**Output:** Not printed. This is returned as an HTTP response when wired into Django URLs.

---

## 58) asyncio (Basic)

```python
import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(say_hello())
```

**Output:**

```text
Hello
World
```

---

## 59) pytest (Example)

```python
def test_addition():
    assert 1 + 1 == 2
```

**Output:** When you run `pytest`, you get a report, e.g.

```text
1 passed in 0.02s
```

---

## 60) tkinter (GUI)

Creates a window. Output is typically not printed unless you add prints.

---

## 61) threading (Two tasks)

```python
import threading

def task1():
    print("Task 1 running")

def task2():
    print("Task 2 running")

thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
```

**Output (order may vary):**

```text
Task 1 running
Task 2 running
```

---

## 62) multiprocessing (Worker)

```python
import multiprocessing

def worker():
    print("Worker process started")

if __name__ == "__main__":
    process = multiprocessing.Process(target=worker)
    process.start()
    process.join()
```

**Output:**

```text
Worker process started
```

---

## 63) subprocess.run

```python
import subprocess

result = subprocess.run(['echo', 'Hello, subprocess!'], capture_output=True, text=True)
print(result.stdout)
```

**Output:**

```text
Hello, subprocess!
```

---

## 64) os + sys (argv + cwd)

```python
import os
import sys

current_directory = os.getcwd()
print(current_directory)

print(sys.argv)
```

**Output (varies):**

```text
C:\Users\YourName\Projects
['script.py']
```

---

## 65) logging

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
```

**Output (format may vary by configuration):**

```text
INFO:root:This is an info message
WARNING:root:This is a warning message
ERROR:root:This is an error message
```

---

## 66) json (Repeat)

Same behavior as section 27.

---

## 67) hashlib (SHA-256)

```python
import hashlib

text = "Hello, world!"
hashed_text = hashlib.sha256(text.encode()).hexdigest()
print(hashed_text)
```

**Output (exact, deterministic):**

```text
315f5bdb76d078c43b8ac0064e4a0164612b1fce77c869345bfc94c75894edd3
```

---

## 68) functools.lru_cache

```python
from functools import lru_cache

@lru_cache(maxsize=3)
def expensive_function(x):
    print(f"Computing {x}...")
    return x * x

print(expensive_function(2))
print(expensive_function(2))
```

**Output:**

```text
Computing 2...
4
4
```

---

## 69) collections.defaultdict

```python
from collections import defaultdict

default_dict = defaultdict(int)
default_dict["apple"] += 1
print(default_dict["apple"])
```

**Output:**

```text
1
```

---

## 70) memoryview

```python
data = bytearray(b"Hello, world!")
view = memoryview(data)
print(view[0])
```

**Output:**

```text
72
```

---

## 71) weakref

```python
import weakref

class MyClass:
    def __del__(self):
        print("MyClass instance deleted")

obj = MyClass()
weak_ref = weakref.ref(obj)
del obj
```

**Output:**

```text
MyClass instance deleted
```

---

## 72) pickle

```python
import pickle

data = {"name": "Alice", "age": 25}
with open("data.pickle", "wb") as f:
    pickle.dump(data, f)

with open("data.pickle", "rb") as f:
    loaded_data = pickle.load(f)

print(loaded_data)
```

**Output:**

```text
{'name': 'Alice', 'age': 25}
```

---

## 73) contextlib.contextmanager

```python
from contextlib import contextmanager

@contextmanager
def my_context_manager():
    print("Entering context")
    yield
    print("Exiting context")

with my_context_manager():
    print("Inside context")
```

**Output:**

```text
Entering context
Inside context
Exiting context
```

---

## 74) uuid

```python
import uuid

generated_uuid = uuid.uuid4()
print(generated_uuid)
```

**Output (varies):**

```text
2f3c14f8-c3d1-4b7b-91c4-076073dfb320
```

---

## 75) inspect.signature

```python
import inspect

def my_function(a, b):
    return a + b

print(inspect.signature(my_function))
```

**Output:**

```text
(a, b)
```

---

## 76) dataclasses

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

person = Person("Alice", 25)
print(person)
```

**Output:**

```text
Person(name='Alice', age=25)
```

---

## 77) threading vs multiprocessing (Example)

```python
import threading
import multiprocessing

def cpu_bound_task():
    print("CPU-bound task")

if __name__ == "__main__":
    thread = threading.Thread(target=cpu_bound_task)
    thread.start()
    thread.join()

    process = multiprocessing.Process(target=cpu_bound_task)
    process.start()
    process.join()
```

**Output:**

```text
CPU-bound task
CPU-bound task
```

---

## 78) asyncio vs threading (Async example)

Same as section 58.

---

## 79) warnings

```python
import warnings
warnings.warn("This is a warning", UserWarning)
```

**Output (format may vary):**

```text
...: UserWarning: This is a warning
```

---

## 80) sqlite3 (users with age)

```python
import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 25)")
conn.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

conn.close()
```

**Output:** Depends on existing rows, e.g.

```text
[(1, 'Alice', 25)]
```

---

## 81) asyncio.gather

```python
import asyncio

async def task_1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 finished")

async def task_2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 finished")

async def main():
    await asyncio.gather(task_1(), task_2())

asyncio.run(main())
```

**Output (timing-based order):**

```text
Task 1 started
Task 2 started
Task 2 finished
Task 1 finished
```

---

## 82) with statement (Write file)

```python
with open("file.txt", "w") as f:
    f.write("Hello, file!")
```

**Output:** None.

---

## 83) itertools.permutations

```python
import itertools

data = [1, 2, 3]
perms = itertools.permutations(data)
print(list(perms))
```

**Output:**

```text
[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
```

---

## 84) subprocess.Popen

```python
import subprocess

process = subprocess.Popen(["echo", "Hello, World!"], stdout=subprocess.PIPE)
stdout, stderr = process.communicate()
print(stdout.decode())
```

**Output:**

```text
Hello, World!
```

---

## 85) shutil.copy (Repeat)

Same behavior as section 44.

---

## 86) enum

```python
from enum import Enum

class Status(Enum):
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3

print(Status.PENDING)
print(Status.PENDING.name)
print(Status.PENDING.value)
```

**Output:**

```text
Status.PENDING
PENDING
1
```

---

## 87) pathlib.Path

```python
from pathlib import Path

path = Path("folder/subfolder/file.txt")
print(path.exists())
print(path.is_file())
print(path.parent)
```

**Output (depends on whether the path exists):**

```text
False
False
folder/subfolder
```

---

## 88) abc (Abstract Base Classes)

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(circle.area())
```

**Output:**

```text
78.5
```

---

## 89) time.perf_counter (Performance)

```python
import time

start_time = time.perf_counter()
for _ in range(1000000):
    pass
end_time = time.perf_counter()

print(f"Execution time: {end_time - start_time} seconds")
```

**Output (varies):**

```text
Execution time: 0.02 seconds
```

---

## 90) traceback

```python
import traceback

try:
    1 / 0
except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc()
```

**Output (traceback details vary by file/line):**

```text
Error: division by zero
Traceback (most recent call last):
  File "...", line X, in <module>
    1 / 0
ZeroDivisionError: division by zero
```

---

## 91) pytest (Repeat)

Same as section 59.

---

## 92) unittest.mock.MagicMock

```python
from unittest.mock import MagicMock

mock = MagicMock()
mock.return_value = 42
print(mock())
```

**Output:**

```text
42
```

---

## 93) os.environ

```python
import os

os.environ["MY_VAR"] = "value"
print(os.environ["MY_VAR"])
```

**Output:**

```text
value
```

---

## 94) tkinter GUI (Repeat)

Window appears. No standard printed output unless you add prints.

---

## 95) requests GET (Repeat)

Same as section 20 / 26.

---

## 96) pandas DataFrame (Repeat)

Same as section 53.

---

## 97) numpy sum

```python
import numpy as np

array = np.array([1, 2, 3, 4, 5])
print(np.sum(array))
```

**Output:**

```text
15
```

---

## 98) scipy stats (Mean/Std Dev)

Your snippet uses `np` but does not show `import numpy as np` in that specific block. Here is the corrected runnable version:

```python
import numpy as np

data = [2.3, 2.9, 3.1, 3.6, 4.2]
mean = np.mean(data)
std_dev = np.std(data)

print(f"Mean: {mean}, Std Dev: {std_dev}")
```

**Output:**

```text
Mean: 3.22, Std Dev: 0.6356099432828283
```

---

## 99) sympy (Solve equation)

```python
from sympy import symbols, Eq, solve

x = symbols('x')
equation = Eq(x**2 + 3*x - 4, 0)
solutions = solve(equation, x)
print(solutions)
```

**Output:**

```text
[-4, 1]
```

---

## 100) multiprocessing.Pool

```python
import multiprocessing

def square(n):
    return n * n

if __name__ == "__main__":
    with multiprocessing.Pool(4) as pool:
        results = pool.map(square, [1, 2, 3, 4, 5])
    print(results)
```

**Output:**

```text
[1, 4, 9, 16, 25]
```

---

## 101) logging (DEBUG)

```python
import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Debug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")
```

**Output (format may vary):**

```text
DEBUG:root:Debug message
INFO:root:Info message
WARNING:root:Warning message
ERROR:root:Error message
CRITICAL:root:Critical message
```

---

## 102) pickle (Repeat)

Same as section 72.

---

## 103) zip()

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")
```

**Output:**

```text
Alice is 25 years old.
Bob is 30 years old.
Charlie is 35 years old.
```

---

## 104) collections (defaultdict, deque, Counter)

```python
from collections import defaultdict, deque, Counter

d = defaultdict(int)
d["apple"] += 1
print(d)

q = deque([1, 2, 3])
q.appendleft(0)
print(q)

counter = Counter(["apple", "banana", "apple", "orange"])
print(counter)
```

**Output:**

```text
defaultdict(<class 'int'>, {'apple': 1})
deque([0, 1, 2, 3])
Counter({'apple': 2, 'banana': 1, 'orange': 1})
```

---

## 105) functools (lru_cache, partial, reduce)

```python
from functools import lru_cache, partial, reduce

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(30))

def multiply(x, y):
    return x * y

double = partial(multiply, 2)
print(double(5))

result = reduce(lambda x, y: x + y, [1, 2, 3, 4])
print(result)
```

**Output:**

```text
832040
10
10
```

---

## 106) memoryview (Modify bytes)

```python
data = bytearray(b"Hello, World!")
view = memoryview(data)

print(view[0])
view[0] = 88
print(data)
```

**Output:**

```text
72
bytearray(b'Xello, World!')
```

---

## 107) namedtuple

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
point = Point(1, 2)

print(point.x)
print(point.y)
```

**Output:**

```text
1
2
```

---

## 108) **slots**

```python
class MyClass:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = MyClass(1, 2)
print(obj.x)
```

**Output:**

```text
1
```

---

## 109) **del** (Object destruction)

```python
class MyClass:
    def __del__(self):
        print("Object is being destroyed!")

obj = MyClass()
del obj
```

**Output:**

```text
Object is being destroyed!
```

---

## 110) assert

```python
x = 5
assert x == 5
# assert x == 6
```

**Output:** None (first assert passes).
If you uncomment `assert x == 6`, you get:

```text
AssertionError
```

---

## 111) contextlib (Repeat)

Same as section 73.

---

## 112) timeit

```python
import timeit

execution_time = timeit.timeit("x = 2 + 2", number=1000000)
print(f"Execution time: {execution_time} seconds")
```

**Output (varies):**

```text
Execution time: 0.05 seconds
```

---

## 113) os.mkdir + os.rmdir

```python
import os

os.mkdir("new_directory")
os.rmdir("new_directory")
```

**Output:** None.
**Note:** `os.rmdir` only removes an empty directory.

---

## 114) dataclasses (Repeat)

Same as section 76.

---

## 115) pdb Debugger (Breakpoint)

```python
import pdb

def my_function(x):
    pdb.set_trace()
    return x * 2

result = my_function(5)
```

**Output (interactive debugger prompt; sample):**

```text
> ...(... )my_function()
-> return x * 2
(Pdb)
```

You can type commands like `n` (next), `p x` (print x), and `c` (continue).

---



