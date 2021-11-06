class Student:   
    def _init_(self,name,email):        
        self.name=name        
        self.email=email   
    def putdata(self):       
        print("\nStudent's details:\nName\t: ",self.name,"\nE-mail\t: ",self.email) 
class PhDGuide:   
    def _init_(self, name, email,students):        
        self.name=name       
        self.email=email        
        self.students=students
    def putdata(self):       
        print("\nGuide Data:\nName\t: ",self.name,"\nE-mail\t: ",self.email)       
        print("\nList of students\n")       
        for s in self.students:
            print("\t",s.name,"\t",s.email) 
    def add(self, student):   
        s=Student()
        s.name=student.name
        s.email=student.email
        if s not in self.students:
            self.students.append(s) 
    def remove(self, student):        
        s=Student()        
        s.name=student.name
        s.email=student.email
        flag=0       
        for s1 in self.students:            
            if(s1.email==s.email):                     
                print(s, " removed")            
            self.students.remove (s1)           
            flag=1        
        if flag==0:           
            print("Not found") 

Harsh=Student() 
Harsh._init_("Harsh","i_harsh_bhasin@yahoo.com")
Nav=Student()
Nav._init_("Nav","i_nav@yahoo.com")
Naks=Student()
Naks._init_("Nakul","nakul@yahoo.com")
print("\nDetails of students\n") 
Harsh.putdata() 
Nav.putdata() 
Naks.putdata() 
KKA=PhDGuide()
KKA._init_("KKA","kka@gmail.com",[])
MU=PhDGuide()
MU._init_("Moin Uddin","prof.moin@yahoo.com",[])
print("Details of Guides") 
KKA.putdata() 
MU.putdata() 
MU.add(Harsh) 
MU.add(Nav) 
KKA.add(Naks) 
print("Details of Guides (after addition of students") 
KKA.putdata() 
MU.putdata() 
MU.remove(Harsh) 
KKA.add(Harsh) 
print("Details of Guides") 
KKA.putdata()  
MU.putdata()
