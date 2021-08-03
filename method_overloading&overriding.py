#Method overloading
#defining the same method name with differ in number of parameters and typ of parameters
class Area:
    
    def find_area(self,a=None,b=None):
        
        if a!=None and b!=None:
            print("Area of Rectangle:",(a*b))
            
        elif a!=None:
            print("Area of square:",(a*a))
            
        else:
            print("Nothing to find")
obj1=Area()
obj1.find_area()
obj1.find_area(12)
obj1.find_area(15,50)


#method overriding



class Parent():
	
	
	def __init__(self):
		self.value = "Inside Parent"
		
	
	def show(self):
		print(self.value)
		

class Child(Parent):
	
	
	def __init__(self):
		self.value = "Inside Child"
		
	
	def show(self):
		print(self.value)
		
		
# Driver's code
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()




class sample:
    def __init__(self,val):
        self.val=val
        
    def display(self):
        
        a=self.val*self.val
        print('Parent class',a)
class sample1(sample):
    def __init__(self,val):
        self.val=val
    
        
    def display(self):
        a=self.val*self.val*self.val
        print('child class',a)
ob=sample(43)
ob1=sample1(23)
ob.display()
ob1.display()
    
        

