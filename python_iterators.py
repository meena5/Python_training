
#Iterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets.
#The iterator object is initialized using the iter() method. It uses the next() method for iteration.

s='python iterators'
iter_obj=iter(s)
for i in range(len(s)):
    print(iter_obj.__next__())

 
