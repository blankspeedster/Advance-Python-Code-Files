class Student:     
    def _init_(self,name):         
        self.name=name     
    def show(self):         
        print("Name\t: "+self.name)     
    def random(self):        
        print("A random method in the base class") 
class RegularStudent(Student):     
    def _init_(self,name):##overrides the base class method and calls the base class method        
        self.age=22     
        Student._init_(self,name)
    def show(self):##redefines the base class method         
        print("Name (derived class)\t: "+self.name+"\nAge\t: "+str(self.age))     
    def random(self):##nothing to do with the base class method        
        print("Random method in the derived class")
naks = Student()
naks._init_("Nakul")
hari = RegularStudent()
hari._init_("Harsh")
naks.show() 
hari.show() 
##The variables can be seen outside the class also 
print(naks.name) 
print(hari.name)
