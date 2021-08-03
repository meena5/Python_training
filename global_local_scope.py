#Global scope

a = "python scope"

def fun():
    print("a inside:", a)


fun()
print("a outside:", a)


#to change local varaible using global keyword
x = "global keyword"

def foo():
    global x
    x = x * 2
    print(x)

foo()


#local scope
#A variable declared inside the function's body or in the local scope is known as a local variable.
def fun():
    y ="local varaible"
    print(y)

fun()
#print(y) it shows error because scope of local variable is within function only
def fun():
    a=10
    b=20
    c=a+b
    print(c)
fun()



#global and local scope
x = "global scope "

def fun():
    global x
    y = "local scope"
    x = x * 2
    print(x)
    print(y)

fun()


#same name for local and global variables

x = 523

def fun():
    x = 1000
    print("local variable x:", x)


fun()
print("global variable x:", x)


#Non local scope
'''Nonlocal variables are used in nested functions whose local scope is not defined.
This means that the variable can be neither in the local nor the global scope.'''
def outer():
    x = "local scope"

    def inner():
        nonlocal x
        x = "nonlocal scope"
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
