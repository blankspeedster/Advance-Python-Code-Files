class Person:    
    def getdata(self):        
        self.name=input("\nEnter Name\t:")        
        self.age=int(input("\nEnter age\t:"))    
    def putdata(self):        
        print("\nName\t:",self.name,"\nAge\t:",str(self.age)) 

class Employee(Person):    
    def getdata(self):       
        Person.getdata(self)        
        self.emp_code=input("\nEnter employee code\t:")    
    def putdata(self):        
        Person.putdata(self)       
        print("\nEmployee Code\t:",self.emp_code) 
        
class Programmer(Employee):     
    def getdata(self):
        Employee.getdata(self)       
        self.language=input("\nEnter Language\t:")    
    def putdata(self):        
        Employee.putdata(self)        
        print("\nLanguage\t:",self.language) 
        
A=Person() 
print("\nA is a person\nEnter data\n") 
A.getdata() 
A.putdata() 
B=Employee() 
print("\nB is an Empoyee and hence a person\nEnter data\n") 
B.getdata() 
B.putdata() 
C=Programmer() 
print("\nC is a programmer hence an employee and employee is a person\nEnter data\n") 
C.getdata() 
C.putdata()
