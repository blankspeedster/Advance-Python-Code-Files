class operations:    
    def _init_(self, number):        
        self.number=number
    def square(self):       
        return (self.number*self.number)     
    def cube(self):       
        return(self.number*self.number*self.number) 

Num1=operations()
Num1._init_(5)
Num2=operations()
Num2._init_(4)
List= [Num1.square, Num1.cube, Num2.square, Num2.cube]
for callable_object in List:
    print(callable_object())
