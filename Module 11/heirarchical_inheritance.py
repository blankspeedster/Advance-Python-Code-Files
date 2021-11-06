##Hierarchies 
class Staff:    
    def getdata(self):        
        self.name=input("\nEnter the name\t:")       
        self.salary=float(input("\nEnter salary\t:"))     
    def putdata(self):       
        print("\nName\t:",self.name,"\nSalary\t:",self.salary) 
        
class Teaching(Staff):     
    def getdata(self):       
        self.subject=input("\nEnter subject\t:")        
        Staff.getdata(self)    
    def putdata(self):        
        Staff.putdata(self)        
        print("\nSubject\t:",self.subject)

class NonTeaching(Staff):     
    def getdata(self):       
        self.department=input("\nEnter department\t:")       
        Staff.getdata(self)     
    def putdata(self):       
        Staff.putdata(self)        
        print("\nDepartment\t:",self.department) 
X=Staff() 
X.getdata() 
X.putdata() 
##Teacher 
Y=Teaching() 
Y.getdata() 
Y.putdata() 
##Non Teaching Staff 
Z=NonTeaching() 
Z.getdata() 
Z.putdata()
