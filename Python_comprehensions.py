#dict comprehension
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]  
  
# but this line shows dict comprehension here  
myDict = { k:v for (k,v) in zip(keys, values)}  
  
# We can use below too

# myDict = dict(zip(keys, values))  
  
print (myDict)


myDict = {x: x**4 for x in [1,2,3,4,5]}
print (myDict)



#list comprehension
l=[i for i in ['a','b','c','d','e']]
print(l)


l=[ord(i) for i in ['a','b','c','d','e']]
print(l)

l=[int(i) for i in [6,9,4,0,2,8,69,89,67,56,34] if i%2!=0]
print(l)

l=[[i for i in ['a','b','c','d','e']] for j in range(10)]
print(l)


#set comprehension
l={i for i in ['a','b','c','d','e','e','e','f','d','a']}
print(l)

l={i for i in [1,6,7,3,6,3,8,5,4]}
print(l)

   
   
