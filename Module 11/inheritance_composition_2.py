class ABC:      
    def show(self):            
        print("show of ABC") 
class XYZ(ABC):
    def show(self):
        print("Something before calling the base class function") 
ABC.show(XYZ) 
print("Something after calling the base class function") 
A = ABC() 
A.show() 
B= XYZ() 
B.show() 
