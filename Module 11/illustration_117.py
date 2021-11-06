class Student:    
    def display(self, something):        
        print("\n"+something)    
    def getdata(self,name,age):        
        name=name       
        age=age        
        print("\nName\t:",name,"\nAge\t:",age) 

##Creating a new student 
Naved=Student() 
name=input("\nEnter the name of the student\t:") 
age=int(input("\nEnter the age of the student\t:")) 
Naved.getdata(name,age)
