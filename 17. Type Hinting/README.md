Type Hinting: This is all the syntatic sugar
Python is dynamically typed language
Does not enforce type at runtime but used in code reviews to show you a message of what a type should be to fit the standard
Typing module.
Type hinting is a tool to use for development to make it easy
Example: 
def add(num1: int, num2: int) -> int:
		return num1 + num2 
(parameter: type) means what it should be
(-> type) the type of the return value. It can be None too.
Can import types for example -- from numbers import Real
from typing import List
Variable typehinting
The union type --> two or more valid types
Optional --> optional types or None, arguments that can left out.
