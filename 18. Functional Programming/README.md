# Functional Programming in Python

## Overview
Functional programming is a programming paradigm where computation is treated as the evaluation of mathematical functions, avoiding changing state and mutable data. Python, though not a purely functional language, supports many functional programming features, making it a versatile tool in a programmer's toolbox.

## Table of Contents
- [Introduction to Functional Programming](#introduction-to-functional-programming)
  - [Key Concepts](#key-concepts)
- [Core Functional Programming Concepts in Python](#core-functional-programming-concepts-in-python)
  - [First-Class Functions](#first-class-functions)
  - [Pure Functions](#pure-functions)
  - [Higher-Order Functions](#higher-order-functions)
  - [Immutability](#immutability)
- [Functional Programming Techniques](#functional-programming-techniques)
  - [Map, Filter, and Reduce](#map-filter-and-reduce)
  - [Lambda Functions](#lambda-functions)
  - [Function Chaining](#function-chaining)
  - [Partial Functions](#partial-functions)
  - [Currying](#currying)
- [Practical Examples and Best Practices](#practical-examples-and-best-practices)
  - [Avoiding Side Effects](#avoiding-side-effects)
  - [Composing Functions](#composing-functions)
- [Conclusion](#conclusion)

## Introduction to Functional Programming

### Key Concepts
- **Computation as Function Evaluation**: Computation is achieved by evaluating functions that produce values and outcomes. This approach encourages organizing code into discrete functions that each accomplish a single task.
- **Programming with Expressions**: Functional programming emphasizes using expressions rather than statements. Outputs from functions are often passed directly into other functions, enabling a concise and clear coding style.
- **No Side Effects**: A key principle in functional programming is avoiding side effects, meaning a function should not modify any external state or variables outside of its scope.
- **First-Class Functions**: Functions in Python are first-class citizens, meaning they can be passed as arguments to other functions, returned from functions, and assigned to variables.
- **Limited Scope and Functionality**: Functions in functional programming are often designed to accomplish a single, well-defined task, ensuring that each function is limited in scope and easy to understand.

## Core Functional Programming Concepts in Python

### First-Class Functions
In Python, functions are first-class citizens. This means they can be treated like any other variable, passed as arguments to other functions, returned from functions, and stored in data structures.

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def shout(text: str) -> str:
    return text.upper()

def whisper(text: str) -> str:
    return text.lower()

def apply_func(func, value):
    return func(value)

print(apply_func(shout, "Python"))  # Output: PYTHON
print(apply_func(whisper, "Python"))  # Output: python
```

### Pure Functions
A pure function is a function that, given the same input, will always return the same output without causing any side effects (e.g., modifying external variables or states).

```python
def add(a: int, b: int) -> int:
    return a + b

# Example of pure function
result = add(2, 3)  # Always returns 5
```

### Higher-Order Functions
Higher-order functions are functions that take other functions as arguments or return them as results.

```python
def increment(x: int) -> int:
    return x + 1

def apply_twice(func, arg):
    return func(func(arg))

print(apply_twice(increment, 3))  # Output: 5
```

### Immutability
Immutability is a core concept in functional programming. This means that once a data structure is created, it cannot be modified.

```python
# Using tuple instead of list to ensure immutability
coordinates = (10, 20)

# Trying to modify a tuple will raise an error
# coordinates[0] = 15  # TypeError: 'tuple' object does not support item assignment
```

## Functional Programming Techniques

### Map, Filter, and Reduce
These three functions are central to functional programming in Python.

- **Map**: Applies a function to all items in an input list.
- **Filter**: Filters elements from an input list that do not satisfy a predicate (a function returning `True` or `False`).
- **Reduce**: Applies a binary function cumulatively to the items of a sequence, from left to right, reducing the sequence to a single value.

```python
from functools import reduce

# Example using map
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))  # Output: [1, 4, 9, 16]

# Example using filter
evens = list(filter(lambda x: x % 2 == 0, numbers))  # Output: [2, 4]

# Example using reduce
product = reduce(lambda x, y: x * y, numbers)  # Output: 24
```

### Lambda Functions
Lambda functions are anonymous functions defined using the `lambda` keyword. They are often used for small, one-off functions.

```python
# A lambda function to add two numbers
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8
```

### Function Chaining
Function chaining refers to passing the output of one function directly into another, enabling concise and readable code.

```python
def square(x):
    return x * x

def increment(x):
    return x + 1

result = increment(square(3))  # Output: 10
```

### Partial Functions
Partial functions allow you to fix a certain number of arguments of a function and generate a new function.

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

# Create a new function that squares a number
square = partial(power, exponent=2)
print(square(4))  # Output: 16
```

### Currying
Currying is a technique of transforming a function that takes multiple arguments into a sequence of functions that each take a single argument.

```python
def multiply(x):
    def inner(y):
        return x * y
    return inner

double = multiply(2)
print(double(5))  # Output: 10
```

## Practical Examples and Best Practices

### Avoiding Side Effects
To follow functional programming principles, avoid side effects by ensuring that functions do not modify external variables or states.

```python
# Avoid side effects by not modifying external variables
def add_to_list(input_list, item):
    return input_list + [item]

original_list = [1, 2, 3]
new_list = add_to_list(original_list, 4)

print(original_list)  # Output: [1, 2, 3]
print(new_list)  # Output: [1, 2, 3, 4]
```

### Composing Functions
Function composition is the process of combining two or more functions to produce a new function. It can be achieved by chaining functions or using decorators.

```python
def compose(f, g):
    return lambda x: f(g(x))

def add_one(x):
    return x + 1

def square(x):
    return x * x

add_one_then_square = compose(square, add_one)
print(add_one_then_square(5))  # Output: 36
```

## Conclusion
Functional programming in Python is a powerful paradigm that emphasizes immutability, pure functions, and function composition. By incorporating these principles into your Python code, you can write more robust, modular, and maintainable programs. This guide covers both the fundamental and advanced concepts of functional programming in Python, providing practical examples to help you apply these techniques effectively in your projects.
