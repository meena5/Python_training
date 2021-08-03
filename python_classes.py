# A Sample class with init method
class sample:

	# init method or constructor
	def __init__(self, var):
		self.var = var

	# Sample Method
	def print(self):
		print('variable value is', self.var)
s = sample(100)
s.print()

#class method
'''Instead of accepting a self parameter, class methods take a cls parameter that points to the class—and not the object instance—when the method is called.

Because the class method only has access to this cls argument, it can’t modify object instance state.
That would require access to self. However, class methods can still modify class state that applies across all instances of the class.'''

#Instance method
'''Through the self parameter, instance methods can freely access attributes and other methods on the same object.
This gives them a lot of power when it comes to modifying an object’s state.

Not only can they modify object state, instance methods can also access the class itself through the self.__class__ attribute.
This means instance methods can also modify class state.'''

#Static method
'''This type of method takes neither a self nor a cls parameter (but of course it’s free to accept an arbitrary number of other parameters).

Therefore a static method can neither modify object state nor class state.
Static methods are restricted in what data they can access - and they’re primarily a way to namespace your methods.'''
class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'
a=MyClass()
print(a.classmethod())
print(a.staticmethod())
print(a.method())#instance method
