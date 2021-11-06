class BaseClass:    
    def method1(self):       
        print("In BaseClass from method1")     
    def method2(self):       
        self.action()

class Derived1(BaseClass):    
    def method1(self):
        print("A new method, has got nothing to do with that of the base class")

class Derived2(BaseClass):    
    def method1(self):       
        print("A method that extends the base class method")   
        BaseClass.method1(self)

class Derived3(BaseClass):     
    def action(self):       
        print("\nImplementing the base class method") 
for className in (Derived1, Derived2, Derived3):
    print("\nClass\t:",className) 
    className().method1() 
X=Derived3() 
X.method2()
