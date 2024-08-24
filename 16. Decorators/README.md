# Python Decorators

## Overview
Decorators in Python provide a powerful mechanism for extending the behavior of functions or methods without modifying their actual code. By "decorating" a function, you can add extra functionality, such as logging, access control, or memoization. This guide will cover the basics of decorators, closures, and the use of the `functools.wraps` utility, along with advanced techniques like passing arguments to decorators and handling both positional and keyword arguments.

## Table of Contents
- [Introduction to Decorators](#introduction-to-decorators)
  - [Why Use Decorators?](#why-use-decorators)
  - [Basic Syntax of Decorators](#basic-syntax-of-decorators)
- [Closures and Nested Functions](#closures-and-nested-functions)
  - [First-Class Functions](#first-class-functions)
  - [Understanding Closures](#understanding-closures)
- [Creating Custom Decorators](#creating-custom-decorators)
  - [Decorators with Arguments](#decorators-with-arguments)
  - [Using `*args` and `**kwargs`](#using-args-and-kwargs)
  - [Maintaining Function Metadata with `functools.wraps`](#maintaining-function-metadata-with-functoolswraps)
- [Advanced Decorator Techniques](#advanced-decorator-techniques)
  - [Decorating Classes and Methods](#decorating-classes-and-methods)
  - [Chaining Multiple Decorators](#chaining-multiple-decorators)

## Introduction to Decorators

### Why Use Decorators?
Decorators allow you to inject or modify the behavior of functions or methods. This can be particularly useful in scenarios where you want to:
- **Add functionality**: Implement additional logic before or after a function runs, such as logging or timing.
- **Enforce access control**: Restrict or control access to certain functions.
- **DRY (Don't Repeat Yourself)**: Avoid repetitive code by applying common functionality across multiple functions.

### Basic Syntax of Decorators
A decorator is typically a function that takes another function as an argument and returns a new function that enhances or modifies the behavior of the original function.

```python
def simple_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

say_hello()
```

Output:
```plaintext
Before function call
Hello!
After function call
```

Here, the `@simple_decorator` syntax is a shorthand for `say_hello = simple_decorator(say_hello)`.

## Closures and Nested Functions

### First-Class Functions
In Python, functions are first-class objects, meaning they can be passed around as arguments, returned from other functions, and assigned to variables.

```python
def add(x, y):
    return x + y

def apply(func, a, b):
    return func(a, b)

result = apply(add, 2, 3)
print(result)  # Output: 5
```

### Understanding Closures
A closure is a function that remembers the environment (variables, functions) in which it was created, even after that environment has gone out of scope.

```python
def outer():
    number = 5
    def inner():
        print(number)
    return inner

closure = outer()
closure()  # Output: 5
```

Here, the `inner` function retains access to the variable `number` even after `outer` has finished execution.

## Creating Custom Decorators

### Decorators with Arguments
Decorators can be customized to accept arguments by nesting the decorator function within another function.

```python
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

Output:
```plaintext
Hello, Alice!
Hello, Alice!
Hello, Alice!
```

### Using `*args` and `**kwargs`
Decorators often need to handle a variable number of positional and keyword arguments. This is where `*args` and `**kwargs` come into play.

```python
def flexible_decorator(func):
    def wrapper(*args, **kwargs):
        print("Arguments:", args)
        print("Keyword Arguments:", kwargs)
        return func(*args, **kwargs)
    return wrapper

@flexible_decorator
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info("Bob", 25)
```

Output:
```plaintext
Arguments: ('Bob', 25)
Keyword Arguments: {}
Name: Bob, Age: 25
```

### Maintaining Function Metadata with `functools.wraps`
When a decorator wraps a function, it can obscure the original function's metadata, such as its name and docstring. The `functools.wraps` decorator is used to preserve this metadata.

```python
from functools import wraps

def preserve_metadata(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        return func(*args, **kwargs)
    return wrapper

@preserve_metadata
def example_function():
    """This is an example function"""
    print("Hello, world!")

print(example_function.__name__)  # Output: example_function
print(example_function.__doc__)   # Output: This is an example function
```

## Advanced Decorator Techniques

### Decorating Classes and Methods
Decorators can also be applied to class methods and even entire classes. When decorating methods, it’s important to use `@classmethod` or `@staticmethod` as appropriate.

```python
def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print(f"Method {func.__name__} called")
        return func(self, *args, **kwargs)
    return wrapper

class MyClass:
    @method_decorator
    def greet(self):
        print("Hello from MyClass!")

obj = MyClass()
obj.greet()
```

Output:
```plaintext
Method greet called
Hello from MyClass!
```

### Chaining Multiple Decorators
You can chain multiple decorators by stacking them on top of a function. The decorators are applied from bottom to top.

```python
def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclaim(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!"
    return wrapper

@exclaim
@uppercase
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))  # Output: HELLO, ALICE!
```

## Conclusion
Decorators are a powerful feature in Python, enabling you to enhance or modify the behavior of functions and methods in a clean, readable way. By understanding how to use closures, handle arguments, and chain decorators, you can apply them effectively in your projects. This guide provides a comprehensive overview of decorators, from basic concepts to advanced techniques, with practical examples to help you implement them in your code.
