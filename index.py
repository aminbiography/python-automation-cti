***Python Code for Automation***

---

## Printing Output

Printing is used to display script results, status messages, and operational information.

```python
print("I code Python!")
print(360)
```

**Output**

```
I code Python!
360
```

Printing computed values:

```python
value = 8 * 6
print(value)
```

**Output**

```
48
```

---

## Arithmetic Operations

### Exponentiation (Power)

```python
print(4 ** 6)
```

**Output**

```
4096
```

### Square Root Calculation

```python
print(4 ** 0.5)
```

**Output**

```
2.0
```

### Basic Arithmetic

```python
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
```

**Output**

```
15
5
50
2.0
```

---

## Variables

Variables store values for later reuse and calculation.

```python
weeks_in_a_year = 52
years = 10
weeks_in_a_decade = years * weeks_in_a_year
print(weeks_in_a_decade)
```

**Output**

```
520
```

---

## Password Combination Calculation

Used to estimate possible authentication combinations.

```python
print(10 ** 3)
```

**Output**

```
1000
```

```python
print(10 ** 6)
```

**Output**

```
1000000
```

---

## Data Usage Calculation

Used in automation for resource and capacity estimation.

```python
download_size_kb = 204800
total_computers = 200
total_kbs = download_size_kb * total_computers
print(total_kbs)
```

**Output**

```
40960000
```

---

## Comments

Comments document intent and improve code readability.

```python
# Display automation status
print("Script executed")
```

**Output**

```
Script executed
```

---

## Data Types

### Integer

```python
users = 25
print(users)
```

**Output**

```
25
```

### Float

```python
cpu_usage = 75.5
print(cpu_usage)
```

**Output**

```
75.5
```

### String

```python
username = "admin"
print(username)
```

**Output**

```
admin
```

### Boolean

```python
is_active = True
print(is_active)
```

**Output**

```
True
```

---

## Type Checking

```python
print(type(100))
print(type(10.5))
print(type("security"))
```

**Output**

```
<class 'int'>
<class 'float'>
<class 'str'>
```

---

## User Input

Used for parameterized scripts.

```python
name = input("Enter operator name: ")
print("Operator:", name)
```

**Input**

```
Amein
```

**Output**

```
Operator: Amein
```

---

## String Operations

### Concatenation

```python
system = "Cyber"
domain = "Security"
print(system + " " + domain)
```

**Output**

```
Cyber Security
```

### Length

```python
print(len("Automation"))
```

**Output**

```
10
```

### Case Conversion

```python
print("admin".upper())
print("ADMIN".lower())
```

**Output**

```
ADMIN
admin
```

---

## Conditional Logic

Used for decision-making in scripts.

```python
password_attempts = 5

if password_attempts > 3:
    print("Access blocked")
else:
    print("Access granted")
```

**Output**

```
Access blocked
```

---

## Comparison Operators

```python
print(5 == 5)
print(5 != 3)
print(10 > 5)
print(10 <= 20)
```

**Output**

```
True
True
True
True
```

---

## Logical Operators

```python
is_admin = True
is_logged_in = False

if is_admin and is_logged_in:
    print("Administrative access")
else:
    print("Restricted access")
```

**Output**

```
Restricted access
```

---

## Loops

### For Loop

```python
for i in range(5):
    print(i)
```

**Output**

```
0
1
2
3
4
```

### While Loop

```python
attempts = 0

while attempts < 3:
    print("Retry attempt")
    attempts += 1
```

**Output**

```
Retry attempt
Retry attempt
Retry attempt
```

---

## Lists

```python
ports = [22, 80, 443]
print(ports)
```

**Output**

```
[22, 80, 443]
```

Iterating through a list:

```python
for port in ports:
    print(port)
```

**Output**

```
22
80
443
```

---

## Dictionaries

```python
user = {
    "username": "admin",
    "role": "administrator",
    "active": True
}

print(user["username"])
```

**Output**

```
admin
```

---

## Functions

Reusable blocks of logic.

```python
def greet(name):
    print("Session started for", name)

greet("Amein")
```

**Output**

```
Session started for Amein
```

Return values:

```python
def add(a, b):
    return a + b

print(add(5, 7))
```

**Output**

```
12
```

---

## Error Handling

Prevents unexpected script termination.

```python
try:
    value = int("abc")
except ValueError:
    print("Input conversion error")
```

**Output**

```
Input conversion error
```

---

## File Reading

```python
with open("data.txt", "r") as file:
    print(file.read())
```

**Output**

```
(file contents displayed)
```

---

## File Writing

```python
with open("output.txt", "w") as file:
    file.write("Automation output generated")
```

**Output**

```
(output.txt written successfully)
```

---

## Why Precision Matters

Computers execute instructions **exactly as written**.

* Ambiguous logic produces unreliable results
* Precision improves automation stability
* Clear code reduces operational risk

---

## What Is Automation?

Automation replaces **manual, repetitive operations** with reliable scripts.

```python
print("Automation task completed")
```

**Output**

```
Automation task completed
```

---

## Syntax vs Semantics

* **Syntax:** Correct structure of code
* **Semantics:** Correct behavior of code

Valid syntax with incorrect logic still produces incorrect results.

---

## Python Characteristics

```python
print("Python is widely used for automation and security scripting")
```

**Output**

```
Python is widely used for automation and security scripting
```

---

## Learning Principle

```python
print("Python is effective for automation tasks")
```

**Output**

```
Python is effective for automation tasks
```

---
---

