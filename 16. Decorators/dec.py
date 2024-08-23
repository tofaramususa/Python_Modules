def logme(func):
	"""Decorator to log the function name"""
	import logging
	logging.basicConfig(level=logging.DEBUG)

	def inner():
		logging.debug("Called {}".format(func.__name__))
		return func()
	return inner

def logme(func):
	"""Decorator to log the function name"""
	import logging
	logging.basicConfig(level=logging.DEBUG)

	def inner(*args, **kwargs):
		logging.debug("Called {} with args {} and kwargs {}".format(func.__name__, args, kwargs))
		return func(*args, **kwargs)
	return inner

# can use at log me at the top of the function
