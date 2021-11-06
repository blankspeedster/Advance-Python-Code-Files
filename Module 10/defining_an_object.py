class employee: 
    def getdata(self):   
        self.name=input('Enter name\t: ')   
        self.age=input('Enter age\t: ') 
    def putdata(self):   
        print('Name\t:',self.name)   
        print('Age\t:',self.age) 
e1=employee() 
e1.getdata() 
e1.putdata()
