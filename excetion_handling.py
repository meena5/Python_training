try:
    a=int(input())
    b=int(input())
    c=a+b
    d=a/b
except ValueError:
    print("enter integers")
except ZeroDivisionError:
    print("Denominator must be greater than zero")
except NameError:
    print("please enter valid name")

except TypeError:
    print("enter valid type values")
finally:
    print("Exceptional Handling")


try:
    a=int(input())
    b=int(input())
    c=a+b
    d=a/b
except ValueError:
    print("enter integers")
except ZeroDivisionError:
    print("Denominator must be greater than zero")
except NameError:
    print("please enter valid name")

except TypeError:
    print("enter valid type values")
else:
    print(c,d)
finally:
    print("Exceptional Handling")

# arguments of an exception


def fun(val):
    try:
        return int(val)
    except Exception as Argument:
        print("Value must be integer",Argument)
print(fun('meena'))
    

    
    
