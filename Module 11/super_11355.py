class BaseClass:    
    def _init_(self, data):        
        self.data=data  
    def printData(self):       
        print("Data of the base class\t:",self.data) 
        
class DerivedClass(BaseClass):    
    def _init_(self,data1, data2):        
        self.data1=data1       
        super(DerivedClass, self)._init_(data2)     
    def printData(self):       
        super(DerivedClass,self).printData()

x=BaseClass()
x._init_(4)
x.printData()

y=DerivedClass()
y._init_(5,6)

print("Data of the derived class\t:",x.printData())
