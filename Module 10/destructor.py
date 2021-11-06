class employee: 
    def getdata(self):   
        self.name=input('Enter name\t: ')   
        self.age=input('Enter age\t: ') 
    def putdata(self):   
        print('Name\t: ',self.name)   
        print('Age\t: ',self.age) 
    def _init_(self, name, age):   
        self.name=name  
        self.age=age 
    def _del_(self):   
        print('Done') 

#e1=employee() 
#e1.getdata() 
#e1.putdata() 
e2=employee()
e2._init_('Naved', 32)
e2.putdata() 
e2._del_() 
