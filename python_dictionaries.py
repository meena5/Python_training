
d = {1: 'A', 2: 'B', 3: 'C'}
print(d)
 
# Creating a Dictionary with Mixed keys
d = {'N': 'G', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(d)

#empty dictionary
d = {}
print(d)
d=dict()
print(d)
 
# Creating a Dictionary with dict() method
d = dict({1: 'G', 2: 'F', 3:'B'})
print(d)
 
# Creating a Dictionary with each item as a Pair
d = dict([(1, 'A'), (2, 'B')])
print(d)

print(list(d.items()))
print(d.keys())
print(d.values())

#nested dictionaries
d = {1: 'A', 2: 'G',
        3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Python'}}
 
print(d)

#adding elements
d[4]='hello'
d[6]='heloooo'
d[5]='B'
print(d)
#accessing elements
print(d.get(3))
print(d.get(4))
#deleting elements
del d[3]
print(d)

#traversing

for i in d.items():
    print(i)

for i in d.keys():
    print(i)

for i in d.values():
    print(i)


#sorting
sorted(d.values())
print(d)
sorted(d.items())
print(d)
sorted(d.keys())
print(d)

#removing dict elements
d.pop(1)
print(d)

d.popitem()# removes last item in the dictionary
print(d)

d.clear()# returns empty dictionary
print(d)



