class BaseClass:    
    def _init_(self,data):        
        self.data=data    
    def show(self):        
        print("\nData\t:",self.data)

class Derived1(BaseClass):    
    def _init_(self,data,data1):        
        self.data1=data1       
        BaseClass._init_(self,data)     
    def show(self):       
        print("\nData\t:",self.data1,"\nBase class data\t:",self.data) 
        
class Derived2(BaseClass):    
    def _init_(self,data,data2):
        self.data2=data2       
        BaseClass._init_(self,data)    
    def show(self):       
        print("\nData\t:",self.data2,"\nBase class data\t:",self.data)
X=BaseClass()
X._init_(1)
X.show() 
print(X.data) 
Y=Derived1()
Y._init_(2, 3)
Y.show() 
Z=Derived2()
Z._init_(4, 5)
Z.show()
