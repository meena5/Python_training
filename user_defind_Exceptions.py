
# derived from super class Exception
class MyError(Exception):
	
	# Constructor or Initializer
	def __init__(self, value):
		self.value = value
	
	# __str__ is to print() the value
	def __str__(self):
		return(repr(self.value))
	
try:
	raise(MyError("Some Error Data"))
	
# Value of Exception is stored in error
except MyError as Argument:
	print('This is the Argument\n', Argument)


########################user defined exceptions

# class Error is derived from super class Exception
class Error(Exception):

	# Error is derived class for Exception, but
	# Base class for exceptions in this module
	pass

class TransitionError(Error):

	# Raised when an operation attempts a state
	# transition that's not allowed.
	def __init__(self, prev, nex, msg):
		self.prev = prev
		self.next = nex

try:
	raise(TransitionError(2, 3 * 2, "Not Allowed"))

# Value of Exception is stored in error
except TransitionError as Argument:
	print('Exception occurred: ', Argument)




