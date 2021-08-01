# A generator-function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return.
def simpleGeneratorFun():
    yield 101            
    yield 202            
    yield 302
    yield 2334
    yield 456
   
# Driver code to check above generator function
for value in simpleGeneratorFun(): 
    print(value)

def gen_fun():
    for i in range(10):
        yield i
for j in gen_fun():
    print(j)

'''Generator-Object : Generator functions return a generator object.
Generator objects are used either by calling the next method on the generator object or using the generator object in a “for in” loop''' 

# returning generator object
def gen_fun():
    for i in range(10):
        yield i
print(gen_fun())

#using next() method to generate a value
def gen_fun():
    for i in range(10):
        yield i
a=gen_fun()
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())

# generator expressions are surrounded by parenthesis ()
l=[1,7,2,4,8,4,7,3,9,23,45,67,19,20]
generator = (x**2 for x in l)
for i in range(len(l)):
    print(generator.__next__())


