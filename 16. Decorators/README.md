Decorators:
Decorators in Python are called "decorators" because they "decorate" or "wrap" a function (or method, or class) with additional functionality without modifying the function's actual code. The term "decorate" in this context refers to the idea of adding something extra to an existing entity, much like how you might decorate a room by adding furniture, artwork, or paint to enhance its appearance or functionality.
Nest functions inside other functions.
def outer()
	number = 5

	def inner():
		print(number)
	inner()

Functions are first class citizens/objects. They can be passed around like variables, as parameters

def apply(func, x, y)
	return function(x, y)

Closure - predefined scope.
def close():
	x = 5
	def inner():
		print(X)
	return inner

closure = close()
closure()

returns pointer to the inner function
private variables
Decorators are functions that accept functions as arguments and have inner functions that perform some action before returning accepted function

Can use the @ keyword. 

Change the decorator to accept arguments.
Args and kwargs: *args and **kwargs are special syntax in Python used for passing a variable number of arguments to a function. Positional and keyword arguments.

python functools wraps -- handles decorator assignments.
@wraps(func) - assign all content from argument passed function to inner function. 