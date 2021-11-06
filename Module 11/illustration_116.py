class Student:    
    def display(self, something):        
        print("\n"+something) 

##Invoking a bound method 
Hari = Student() 
Hari.display("Hi I am Hari") 
##display() can also be invoked through an instance of the method 
X= Hari.display 
X("Hi I am through X") 
##display called again 
Student().display("Caling diaplay again")
