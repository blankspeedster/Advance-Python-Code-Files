class demo_class:  
    a=5 
    def getdata(self,b):   
        a=7;  
        self.b=b
    def putdata(self):  
        print("The value of \a\ is", a, " and that of\b\is ",self.b) 
d=demo_class() 
d.getdata(9) 
d.putdata() 
