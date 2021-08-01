s={1,6,3,8,4,8,3,8,4,5,0}
print(s)

s=set()
s={}
print(s)

s=set([1,6,3,4,'h','r',7,3,7])
print(s)


# set methods

s.add('abc')
print(s)

s.remove('h')
print(s)

s1={'a','o','e','d','ajds','gfh',2,1,7,3,'r'}
s2=s.union(s1)
print(s2)


s2=s.intersection(s1)
print(s2)

s2=s.difference(s1)
print(s2)

# subset and superset
if s1>s2:
    print("s1 is superset of s2")
else:
    print("s1 is subset of s2")

# or
if s.issuperset(s1):
    print("s1")
else:
    print("s2")

if s.issubset(s1):
    print("s1")
else:
    print("s2")


# disjoint sets
if s.isdisjoint(s1):
    print("yes")
else:
    print("no")

s2.clear()

print(s2)
    

# A frozen set(immutable)
frozen_set = frozenset(["e", "f", "g"])

print(frozen_set)
#frozen_set.add('m')
print(frozen_set)

print("--------------------------------------------------shallow copy and deep copy--------------------------------------------------")

