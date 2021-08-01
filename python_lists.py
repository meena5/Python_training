
l=[4,6,5,7,8,2,4,6,8,9,10,29,48,59]
l.append(8)
print(l)

l.insert(4,90)
print(l)

print(l.index(5))

print(l.count(8))

l.sort()
print(l)

l.reverse()
print(l)

print(sum(l))

l.pop(4)
print(l)

l.remove(8)
print(l)

print([i**2 for i in l])

l1=[2,6,9,7,6,4,3,7,9,4,5,7]
l.extend(l1)
print(l)

del l[2:7]
print(l)

l.clear()
print(l)
print("------------------NESTED LISTS----------------------")
l2=[1,3,7,['a','f','g'],23]
print(l2)

print("-----------------------------------------IMPLICIT TYPE CASTING-----------------------")

x = 10
 
print("x is of type:",type(x))
 
y = 10.6
print("y is of type:",type(y))
 
x = x + y
 
print(x)



print("------------------------------------EXPILCIT TYPE CASTING--------------------------")
s = "10010"
 
# printing string converting to int base 2
c = int(s,2)
print ("After converting to integer base 2 : ", end="")
print (c)
 
# printing string converting to float
e = float(s)
print ("After converting to float : ", end="")
print (e)
print("x is of type:",type(x))





s = '4'
 
# printing character converting to integer
c = ord(s)
print ("After converting character to integer : ",end="")
print (c)
 
# printing integer converting to hexadecimal string
c = hex(56)
print ("After converting 56 to hexadecimal string : ",end="")
print (c)
 
# printing integer converting to octal string
c = oct(56)
print ("After converting 56 to octal string : ",end="")
print (c)
