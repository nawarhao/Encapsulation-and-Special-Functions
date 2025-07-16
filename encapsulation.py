#Class creation
class myClass:
    
    #private variable
    __privateVar = 27
        
        #private method
    def __privMeth(self):
        print("I'm inside class myClass")
        
    #Function to print value of private variable
    def hello(self):
        print("Private variable value:", myClass.__privateVar)
        

#object creation and method call
foo = myClass()
foo.hello()
foo.__privMeth

#Encapsulation, in object-oriented programming, is the mechanism of bundling the data (variables) and the methods (functions) that operate on that data into a single unit, known as a class. It also involves restricting direct access to some of an object's components, protecting the data from unauthorized modification. Think of it as a protective shield around your data, controlling how it's accessed and modified.

