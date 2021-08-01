
def sum_fun():
    l=[1,6,3,7,3,73,7,10,9,3]
    s=0
    for i in l:
        s=s+i
    print(s)
sum_fun()

# default arguments

def add(a,b=5,c=10):
    print(a*b+c)
add(1)
add(2,5)
add(2,5,8)

#keyword arguments
add(b=10,c=15,a=20)
add(b=10,a=2)

#positional arguments
def add(a,b,c):
    print(a*b+c)
add(10,20,30)

'''default arguments should follow non-default arguments
#def add(a=5,b,c): error will occur
    #return (a+b+c)'''


'''def add(a,b,c):
    #return (a+b+c)

#print (add(a=10,3,4))
#Output:SyntaxError: positional argument follows keyword argument'''




#variable-length arguments
#Special Symbols Used for passing arguments:-

#*args (Non-Keyword Arguments)

#**kwargs (Keyword Arguments)
def add(*b):
    result=0
    for i in b:
         result=result+i
    return result

print (add(1,2,3,4,5))



#arbitary functions for keyword arguments

def fn(**a):
    for i in a.items():
        print (i)
fn(numbers=5,colors="blue",fruits="apple")


def fun(**l):
    for i in l.items():
        print(i)       
fun(a=0,b=1)





def myFun(*args,**kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
 

myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks")




#lambda functions

double = lambda x: x * 2

print(double(5))

#In Python, we generally use it as an argument to a higher-order function (a function that takes in other functions as arguments).
#Lambda functions are used along with built-in functions like filter(), map()
# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)

# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)


#nested functions

def fun1(l):
    l1=l[::-1]
    def fun2(l1):
        print(sum(l1))
    fun2(l1)
    print(l1)
l=[1,6,5,2,8,4,9,2,7,9,0]
print(fun1(l))



#high-order functions
#A function is called Higher Order Function if it contains other functions as a parameter or returns a function as an output i.e,
#the functions that operate with another function are known as Higher order Functions

s="high order functions"
def high_order(s):
    a=s.upper()
    b=s.lower()
    return a,b
print(high_order(s))



