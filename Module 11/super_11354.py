class Student:    
    def _init_(self,name):        
        self.name=name
    def putdata(self):        
        print("name\t:",self.name) 
Hari=Student()
Hari._init_("Hari")
Hari.putdata() 
Naks=Student()
Naks._init_("Nakul")
Naks.putdata() 
