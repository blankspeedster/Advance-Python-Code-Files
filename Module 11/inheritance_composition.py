class ABC:
    def show(self):
        print("show of ABC")
class XYZ(ABC):      
    def show1(self):            
        print("show of XYZ") 
A = ABC() 
A.show() 
B= XYZ() 
B.show() 
B.show1() 
