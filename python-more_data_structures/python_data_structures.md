# 🐍 Python Data Structures — Complete Study Guide

> **Scope:** Lists · Tuples · Sequences · Comprehensions · `del` statement  
> **Level:** Beginner-friendly with practical examples  
> **Goal:** Understand every concept deeply before your course tasks

---

## Table of Contents

1. [What Are Lists?](#1-what-are-lists)
2. [Strings vs Lists — Differences & Similarities](#2-strings-vs-lists--differences--similarities)
3. [Most Common List Methods](#3-most-common-list-methods)
4. [Lists as Stacks and Queues](#4-lists-as-stacks-and-queues)
5. [List Comprehensions](#5-list-comprehensions)
6. [What Are Tuples?](#6-what-are-tuples)
7. [Tuples vs Lists — When to Use Each](#7-tuples-vs-lists--when-to-use-each)
8. [What Is a Sequence?](#8-what-is-a-sequence)
9. [Tuple Packing](#9-tuple-packing)
10. [Sequence Unpacking](#10-sequence-unpacking)
11. [The `del` Statement](#11-the-del-statement)
12. [Quick Reference Cheat Sheet](#12-quick-reference-cheat-sheet)

---

## 1. What Are Lists?

A **list** is an ordered, mutable (changeable) collection of items.  
You can store anything inside a list: numbers, strings, booleans, other lists — even mixed types.

### Syntax

```python
# Empty list
my_list = []

# List of numbers
scores = [10, 25, 38, 47]

# List of strings
fruits = ["apple", "banana", "cherry"]

# Mixed types (valid in Python!)
mixed = [1, "hello", True, 3.14]

# Nested list (list inside a list)
matrix = [[1, 2], [3, 4], [5, 6]]
```

### Accessing Items — Indexing

Lists are **zero-indexed**: the first item is at position `0`.

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])   # "apple"   ← first item
print(fruits[1])   # "banana"  ← second item
print(fruits[-1])  # "cherry"  ← last item (negative index goes backwards)
print(fruits[-2])  # "banana"  ← second to last
```

### Slicing — Getting a Sub-list

```python
numbers = [0, 1, 2, 3, 4, 5]

print(numbers[1:4])   # [1, 2, 3]   ← from index 1 up to (not including) 4
print(numbers[:3])    # [0, 1, 2]   ← from the start up to index 3
print(numbers[3:])    # [3, 4, 5]   ← from index 3 to the end
print(numbers[::2])   # [0, 2, 4]   ← every 2 steps
print(numbers[::-1])  # [5, 4, 3, 2, 1, 0]  ← reversed!
```

### Modifying Items

Lists are **mutable** — you can change them after creation.

```python
fruits = ["apple", "banana", "cherry"]

fruits[1] = "mango"
print(fruits)  # ["apple", "mango", "cherry"]
```

### Checking Length

```python
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # 3
```

---

## 2. Strings vs Lists — Differences & Similarities

Both strings and lists are **sequences** in Python. They share several behaviors, but have important differences.

### ✅ Similarities

| Feature | String | List |
|---|---|---|
| Ordered | ✅ Yes | ✅ Yes |
| Zero-indexed | ✅ Yes | ✅ Yes |
| Supports slicing | ✅ Yes | ✅ Yes |
| Supports `len()` | ✅ Yes | ✅ Yes |
| Iterable (usable in loops) | ✅ Yes | ✅ Yes |
| Supports `in` operator | ✅ Yes | ✅ Yes |

```python
# Both support indexing
name = "Marcelo"
fruits = ["M", "a", "r", "c", "e", "l", "o"]

print(name[0])    # "M"
print(fruits[0])  # "M"

# Both support slicing
print(name[0:3])    # "Mar"
print(fruits[0:3])  # ["M", "a", "r"]

# Both support `in`
print("a" in name)      # True
print("a" in fruits)    # True

# Both work in for loops
for char in name:
    print(char)  # M, a, r, c, e, l, o
```

### ❌ Key Differences

| Feature | String | List |
|---|---|---|
| Mutable (changeable)? | ❌ No — immutable | ✅ Yes — mutable |
| Item type | Characters only | Any type |
| Methods available | String-specific | List-specific |

```python
# Strings are IMMUTABLE — you cannot change a character
name = "Marcelo"
name[0] = "m"  # ❌ TypeError: 'str' object does not support item assignment

# Lists are MUTABLE — you can change items freely
fruits = ["apple", "banana"]
fruits[0] = "mango"  # ✅ Works fine
print(fruits)  # ["mango", "banana"]
```

```python
# Converting between them
word = "hello"

# String → List of characters
chars = list(word)
print(chars)  # ['h', 'e', 'l', 'l', 'o']

# List of strings → single string (join)
words = ["Hello", "world"]
sentence = " ".join(words)
print(sentence)  # "Hello world"
```

---

## 3. Most Common List Methods

### `.append(item)` — Add to the end

```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # ["apple", "banana", "cherry"]
```

### `.insert(index, item)` — Add at a specific position

```python
fruits = ["apple", "cherry"]
fruits.insert(1, "banana")  # insert "banana" at index 1
print(fruits)  # ["apple", "banana", "cherry"]
```

### `.extend(iterable)` — Add multiple items

```python
fruits = ["apple", "banana"]
more = ["cherry", "mango"]
fruits.extend(more)
print(fruits)  # ["apple", "banana", "cherry", "mango"]

# Difference from append:
fruits2 = ["apple"]
fruits2.append(["cherry", "mango"])   # adds the LIST as one item
print(fruits2)  # ["apple", ["cherry", "mango"]]  ← nested!

fruits3 = ["apple"]
fruits3.extend(["cherry", "mango"])   # adds each item individually
print(fruits3)  # ["apple", "cherry", "mango"]  ← flat!
```

### `.remove(item)` — Remove by value

```python
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # ["apple", "cherry"]

# If the item doesn't exist → ValueError
fruits.remove("mango")  # ❌ ValueError: list.remove(x): x not in list
```

### `.pop(index)` — Remove by position and return it

```python
fruits = ["apple", "banana", "cherry"]

last = fruits.pop()      # removes the last item
print(last)              # "cherry"
print(fruits)            # ["apple", "banana"]

first = fruits.pop(0)    # removes item at index 0
print(first)             # "apple"
print(fruits)            # ["banana"]
```

### `.index(item)` — Find the position of a value

```python
fruits = ["apple", "banana", "cherry"]
pos = fruits.index("banana")
print(pos)  # 1
```

### `.count(item)` — Count how many times a value appears

```python
numbers = [1, 2, 3, 2, 2, 4]
print(numbers.count(2))  # 3
print(numbers.count(9))  # 0
```

### `.sort()` — Sort in place

```python
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 9]

# Reverse order
numbers.sort(reverse=True)
print(numbers)  # [9, 5, 4, 3, 2, 1, 1]

# Sorting strings
names = ["Zara", "Ana", "Carlos"]
names.sort()
print(names)  # ["Ana", "Carlos", "Zara"]
```

### `sorted()` — Sort and return a new list (original unchanged)

```python
numbers = [3, 1, 4, 1, 5]
new_sorted = sorted(numbers)
print(new_sorted)  # [1, 1, 3, 4, 5]
print(numbers)     # [3, 1, 4, 1, 5]  ← unchanged!
```

### `.reverse()` — Reverse in place

```python
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)  # ["cherry", "banana", "apple"]
```

### `.copy()` — Create a shallow copy

```python
original = [1, 2, 3]
copy = original.copy()

copy.append(4)
print(original)  # [1, 2, 3]  ← not affected
print(copy)      # [1, 2, 3, 4]
```

> ⚠️ **Why not just do `copy = original`?**  
> That creates a **reference**, not a copy. Both variables would point to the **same** list.

```python
original = [1, 2, 3]
reference = original      # ← same object in memory!
reference.append(4)
print(original)  # [1, 2, 3, 4]  ← original is also changed!
```

### `.clear()` — Remove all items

```python
fruits = ["apple", "banana"]
fruits.clear()
print(fruits)  # []
```

---

## 4. Lists as Stacks and Queues

### Stack — Last In, First Out (LIFO)

Think of a stack of plates: you always add and remove from the **top**.

```
Add:    [plate1] → [plate1, plate2] → [plate1, plate2, plate3]
Remove: [plate1, plate2, plate3] → [plate1, plate2] → [plate1]
```

In Python, use `.append()` to push and `.pop()` to pop:

```python
stack = []

# PUSH (add to top)
stack.append("plate1")
stack.append("plate2")
stack.append("plate3")
print(stack)  # ["plate1", "plate2", "plate3"]

# POP (remove from top)
top = stack.pop()
print(top)    # "plate3"  ← last in, first out
print(stack)  # ["plate1", "plate2"]
```

**Real use case:** undo history in a text editor.

```python
history = []

history.append("typed 'Hello'")
history.append("typed ' World'")
history.append("deleted last word")

# User presses Ctrl+Z (undo)
last_action = history.pop()
print(f"Undoing: {last_action}")  # "Undoing: deleted last word"
```

---

### Queue — First In, First Out (FIFO)

Think of a line at the supermarket: first person in, first person served.

```
Add:    [A] → [A, B] → [A, B, C]
Remove: [A, B, C] → [B, C] → [C]
```

You **can** use a list as a queue, but it is **inefficient** — removing from the front (`pop(0)`) requires shifting every other element.

**The right tool:** use `collections.deque`

```python
from collections import deque

queue = deque()

# ENQUEUE (add to the back)
queue.append("customer_A")
queue.append("customer_B")
queue.append("customer_C")
print(queue)  # deque(['customer_A', 'customer_B', 'customer_C'])

# DEQUEUE (remove from the front)
first = queue.popleft()
print(first)   # "customer_A"  ← first in, first out
print(queue)   # deque(['customer_B', 'customer_C'])
```

> 💡 `deque.popleft()` is O(1) — instant.  
> `list.pop(0)` is O(n) — slow on large lists because every item shifts.

---

## 5. List Comprehensions

A **list comprehension** is a concise, readable way to create a new list from an existing one (or any iterable).

### Basic Syntax

```python
new_list = [expression for item in iterable]
```

### Without comprehension (old way)

```python
numbers = [1, 2, 3, 4, 5]
squares = []
for n in numbers:
    squares.append(n ** 2)
print(squares)  # [1, 4, 9, 16, 25]
```

### With comprehension (Pythonic way)

```python
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print(squares)  # [1, 4, 9, 16, 25]
```

### With a Condition (filter)

```python
new_list = [expression for item in iterable if condition]
```

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Only even numbers
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4, 6, 8]

# Only numbers greater than 4
big = [n for n in numbers if n > 4]
print(big)  # [5, 6, 7, 8]
```

### Transforming Strings

```python
words = ["hello", "world", "python"]

# Uppercase all words
upper = [w.upper() for w in words]
print(upper)  # ["HELLO", "WORLD", "PYTHON"]

# Get only words longer than 4 characters
long_words = [w for w in words if len(w) > 4]
print(long_words)  # ["hello", "world", "python"]
```

### Practical Examples

```python
# Scores above passing grade
scores = [45, 72, 88, 31, 95, 60]
passing = [s for s in scores if s >= 60]
print(passing)  # [72, 88, 95, 60]

# Convert Celsius to Fahrenheit
celsius = [0, 20, 37, 100]
fahrenheit = [(c * 9/5) + 32 for c in celsius]
print(fahrenheit)  # [32.0, 68.0, 98.6, 212.0]

# Extract first letters
names = ["Alice", "Bob", "Carlos"]
initials = [name[0] for name in names]
print(initials)  # ["A", "B", "C"]
```

> 💡 **Rule of thumb:** if your loop body is a single line that appends to a list, it's a perfect candidate for a comprehension.

---

## 6. What Are Tuples?

A **tuple** is an ordered, **immutable** (unchangeable) collection of items.  
Syntax uses parentheses `()` instead of brackets `[]`.

```python
# Empty tuple
empty = ()

# Tuple with items
coordinates = (10, 20)
person = ("Marcelo", 38, "Luxembourg")
mixed = (1, "hello", True, 3.14)
```

### Accessing Items — Same as Lists

```python
person = ("Marcelo", 38, "Luxembourg")

print(person[0])   # "Marcelo"
print(person[-1])  # "Luxembourg"
print(person[1:])  # (38, "Luxembourg")
```

### Tuples Are Immutable

```python
person = ("Marcelo", 38, "Luxembourg")
person[1] = 39  # ❌ TypeError: 'tuple' object does not support item assignment
```

You **cannot** add, remove, or change items in a tuple after creation.

### Single-Item Tuple — The Trailing Comma

This is a common mistake:

```python
not_a_tuple = ("hello")   # This is just a string in parentheses!
print(type(not_a_tuple))  # <class 'str'>

real_tuple = ("hello",)   # ← trailing comma makes it a tuple
print(type(real_tuple))   # <class 'tuple'>

# Also valid without parentheses (see Tuple Packing section)
also_tuple = "hello",
print(type(also_tuple))   # <class 'tuple'>
```

### Tuple Methods

Tuples only have 2 methods (because they can't be modified):

```python
numbers = (1, 2, 3, 2, 4, 2)

print(numbers.count(2))   # 3  ← how many times 2 appears
print(numbers.index(3))   # 2  ← position of first occurrence of 3
```

---

## 7. Tuples vs Lists — When to Use Each

| Situation | Use |
|---|---|
| Data that should NOT change (coordinates, RGB colors, config values) | **Tuple** |
| Data that will grow or change (shopping cart, log entries) | **List** |
| Dictionary keys (must be hashable/immutable) | **Tuple** |
| Returning multiple values from a function | **Tuple** |
| Homogeneous sequence of similar items | **List** |
| Heterogeneous record (like a row from a database) | **Tuple** |
| Performance matters and data is fixed | **Tuple** (slightly faster) |

### Practical Examples

```python
# ✅ Use TUPLE: GPS coordinates (they don't change)
location = (49.5231, 5.8982)  # Differdange, Luxembourg

# ✅ Use TUPLE: RGB color
red = (255, 0, 0)

# ✅ Use TUPLE: returning multiple values from a function
def get_user_info():
    return "Marcelo", 38, "Luxembourg"  # Python returns this as a tuple

name, age, country = get_user_info()

# ✅ Use LIST: a dynamic collection
cart = ["laptop", "mouse"]
cart.append("keyboard")  # changes over time

# ✅ Use TUPLE: dictionary key (lists can't be dict keys)
locations = {}
locations[(49.5231, 5.8982)] = "Differdange"  # ✅ tuple as key
# locations[[49.5231, 5.8982]] = "Differdange"  # ❌ list can't be a dict key
```

### Memory Comparison

```python
import sys

my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print(sys.getsizeof(my_list))   # 120 bytes (approximately)
print(sys.getsizeof(my_tuple))  # 80 bytes (approximately)
# Tuples are smaller and slightly faster
```

---

## 8. What Is a Sequence?

A **sequence** is any ordered collection of items that supports:
- **Indexing** — access by position: `seq[0]`
- **Slicing** — sub-selection: `seq[1:3]`
- **Length** — `len(seq)`
- **Iteration** — usable in `for` loops
- **Membership test** — `item in seq`

### Python Sequence Types

| Type | Mutable? | Example |
|---|---|---|
| `list` | ✅ Yes | `[1, 2, 3]` |
| `tuple` | ❌ No | `(1, 2, 3)` |
| `str` | ❌ No | `"hello"` |
| `range` | ❌ No | `range(5)` |
| `bytes` | ❌ No | `b"hello"` |

```python
# All sequences share the same behaviors:

my_list  = [10, 20, 30]
my_tuple = (10, 20, 30)
my_str   = "abc"

# Indexing
print(my_list[0])   # 10
print(my_tuple[0])  # 10
print(my_str[0])    # "a"

# Slicing
print(my_list[1:])   # [20, 30]
print(my_tuple[1:])  # (20, 30)
print(my_str[1:])    # "bc"

# len()
print(len(my_list))   # 3
print(len(my_tuple))  # 3
print(len(my_str))    # 3

# in operator
print(20 in my_list)    # True
print(20 in my_tuple)   # True
print("b" in my_str)    # True
```

> 💡 **Key insight:** When you learn something about sequences (like slicing), it applies to ALL sequence types — strings, lists, tuples, and ranges.

---

## 9. Tuple Packing

**Tuple packing** is when you assign multiple values to a single tuple variable without using parentheses explicitly. Python automatically "packs" the values into a tuple.

```python
# Explicit tuple (with parentheses)
point = (10, 20)

# Tuple PACKING (no parentheses needed — Python packs automatically)
point = 10, 20
print(point)        # (10, 20)
print(type(point))  # <class 'tuple'>
```

### More Examples

```python
# Packing three values
person = "Marcelo", 38, "Luxembourg"
print(person)  # ("Marcelo", 38, "Luxembourg")

# Packing in a function return
def get_min_max(numbers):
    return min(numbers), max(numbers)  # packing two values

result = get_min_max([3, 1, 9, 4, 7])
print(result)  # (1, 9)
```

---

## 10. Sequence Unpacking

**Sequence unpacking** is the reverse of packing: you assign items from a sequence to individual variables in a single line.

### Basic Unpacking

```python
# Unpack a tuple into individual variables
point = (10, 20)
x, y = point
print(x)  # 10
print(y)  # 20

# Unpack a list
colors = ["red", "green", "blue"]
first, second, third = colors
print(first)   # "red"
print(second)  # "green"
print(third)   # "blue"
```

> ⚠️ The number of variables must match the number of items — otherwise you get a `ValueError`.

```python
a, b = (1, 2, 3)  # ❌ ValueError: too many values to unpack
a, b, c, d = (1, 2, 3)  # ❌ ValueError: not enough values to unpack
```

### Unpacking with `*` (star/splat operator)

The `*` captures the remaining items into a list:

```python
numbers = [1, 2, 3, 4, 5]

first, *rest = numbers
print(first)  # 1
print(rest)   # [2, 3, 4, 5]

*start, last = numbers
print(start)  # [1, 2, 3, 4]
print(last)   # 5

first, *middle, last = numbers
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5
```

### Swap Variables Without a Temp Variable

This is a classic Python trick using unpacking:

```python
a = 10
b = 20

# Old way (other languages)
# temp = a
# a = b
# b = temp

# Pythonic way
a, b = b, a
print(a)  # 20
print(b)  # 10
```

### Unpacking in For Loops

Very common with lists of tuples:

```python
employees = [("Alice", 50000), ("Bob", 60000), ("Carlos", 55000)]

for name, salary in employees:
    print(f"{name} earns ${salary:,}")

# Output:
# Alice earns $50,000
# Bob earns $60,000
# Carlos earns $55,000
```

### Ignoring Values with `_`

Use `_` as a throwaway variable for values you don't need:

```python
person = ("Marcelo", 38, "Luxembourg", "Data Analyst")
name, _, country, _ = person
print(name)     # "Marcelo"
print(country)  # "Luxembourg"
```

---

## 11. The `del` Statement

The `del` statement **deletes** things: list items, slices, variables, or dictionary keys.

### Delete a List Item by Index

```python
fruits = ["apple", "banana", "cherry", "mango"]

del fruits[1]       # delete "banana"
print(fruits)       # ["apple", "cherry", "mango"]

del fruits[-1]      # delete last item
print(fruits)       # ["apple", "cherry"]
```

### Delete a Slice

```python
numbers = [0, 1, 2, 3, 4, 5]

del numbers[2:4]    # delete items at index 2 and 3
print(numbers)      # [0, 1, 4, 5]
```

### Clear the Entire List

```python
fruits = ["apple", "banana", "cherry"]
del fruits[:]       # delete all items
print(fruits)       # []
```

### Delete the Variable Itself

```python
x = 42
print(x)   # 42
del x
print(x)   # ❌ NameError: name 'x' is not defined
```

### `del` vs `.remove()` vs `.pop()`

| Method | Removes by | Returns the removed item? |
|---|---|---|
| `del list[i]` | Index | ❌ No |
| `list.pop(i)` | Index | ✅ Yes |
| `list.remove(v)` | Value | ❌ No |

```python
fruits = ["apple", "banana", "cherry"]

# del — removes by index, returns nothing
del fruits[0]
print(fruits)   # ["banana", "cherry"]

# pop — removes by index, RETURNS the item
fruits = ["apple", "banana", "cherry"]
removed = fruits.pop(0)
print(removed)  # "apple"
print(fruits)   # ["banana", "cherry"]

# remove — removes by VALUE, returns nothing
fruits = ["apple", "banana", "cherry"]
fruits.remove("apple")
print(fruits)   # ["banana", "cherry"]
```

---

## 12. Quick Reference Cheat Sheet

### List Operations

```python
lst = [1, 2, 3]

lst.append(4)       # [1, 2, 3, 4]
lst.insert(1, 99)   # [1, 99, 2, 3, 4]
lst.extend([5, 6])  # [1, 99, 2, 3, 4, 5, 6]
lst.remove(99)      # [1, 2, 3, 4, 5, 6]
lst.pop()           # returns 6, list: [1, 2, 3, 4, 5]
lst.pop(0)          # returns 1, list: [2, 3, 4, 5]
lst.sort()          # [2, 3, 4, 5]
lst.reverse()       # [5, 4, 3, 2]
lst.index(3)        # 2
lst.count(3)        # 1
lst.copy()          # [5, 4, 3, 2] (new list)
lst.clear()         # []
len(lst)            # 0
```

### Comprehension Formula

```python
# Basic
[expr for item in iterable]

# With filter
[expr for item in iterable if condition]

# With transformation + filter
[expr for item in iterable if condition]
```

### Packing & Unpacking

```python
# Packing
coords = 10, 20           # → (10, 20)

# Unpacking
x, y = coords             # x=10, y=20

# Star unpacking
first, *rest = [1,2,3,4]  # first=1, rest=[2,3,4]

# Swap
a, b = b, a
```

### Tuple vs List at a Glance

```python
my_list  = [1, 2, 3]   # mutable, brackets
my_tuple = (1, 2, 3)   # immutable, parentheses

my_list[0] = 99   # ✅ works
my_tuple[0] = 99  # ❌ TypeError
```

### `del` Quick Reference

```python
del lst[i]     # delete item at index i
del lst[i:j]   # delete slice
del lst[:]     # clear all items
del variable   # delete variable from memory
```

---

*Study tip: run every example in a Python REPL or Jupyter Notebook. Reading is not enough — type it, break it, and fix it.*
