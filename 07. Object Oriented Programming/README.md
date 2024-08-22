Object Oriented Programming:
Part 1 -
Everything is an object.
Researching and Experimenting
Class has attributes and methods.
The an instance of the class.
Class is a special name. We use upperclas
Can import a class. from a file
Use the constructor
Access members through the dot syntax
del keyword can delete objects therefore they can delete everything.
Then there are functions/methods that are called by the class.
'self' word represents a instance of the class. Self is like self.
__init__ method is the constructor method. How the class is initialised. --> constructor coming from C++.
**kwargs is a dictionary of key value pairs. The setattr

Software Design - logical grouping. Class is also a way of grouping it too.
Organising functions and methods together into a class.  
Focus on leanness. Simple, clean code that works and does the job.

Inheritance: DRY
class className(superClass):
	function body
Get and add on top of everything from the derived class.
Even overriding the previous.
Everything inherits from the 'object'
Super() function. Control the overriding. Access to the super class/ derived class/base class
super() is typically used to call the __init__ method of a parent class, ensuring that the initialization process defined in the parent class is executed in addition to any additional initialization in the child class.
Refactor - improving, modifying, changing the code.
Method Resolution order -- 
function - isinstance(), issubclass(subclass, superclass)
type() tells the object
Magic attributes. 
Meta Programming
Magic methods -- __dunder___ methods
__str__-> return a string representation of the class. Basically how they are represented in different formats like int with int(), floar, init,
then there are operations -- __add__ which takes self and other too.
__radd_ method
Making your own datatype like list-like objects.
Other magic methods -- __iter__, __getitem__, 
The yield keyword, return a function but continue to run the exection -- yield from list. 
__init__ and ___new__ --> getattribute function that is called when we have a dot called on an object 
Class Methods - @classmethod @--decorator, takes a function, does something with that function and returns something. 
Ensure something is not accessible outside the function -- we use the __with the variable. 
use the dir() method.
prot.Protected__method()
use the @property decorator  
Setter to set the property we are decorating @property.setter. Getter and setter for our properties.



Notes:
https://chatgpt.com/share/d6c5b550-4159-4bcd-9490-94cc81a96e96