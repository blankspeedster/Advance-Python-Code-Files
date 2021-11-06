class employee: 
    """The employee class""" 
    def getdata(self):  
        self.name=input('Enter name\t: ')  
        self.age=input('Enter age\t: ')  
    def putdata(self):  
        print('Name\t:',self.name) 
        print('Age\t:',self.age) 
    def _init_(self):
        self.name='ABC'   
        self.age=20 
e1 = employee() 
e1.getdata() 
e1.putdata() 
print(e1.__doc__) 
