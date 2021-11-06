class demo_class:
    a=5
    def getdata(self,b):
        c=7;
        self.b=b
        print('\'c\' is ',c,' and \'b\' is ',self.b)
    def other_function(self):
        c=3
        print('Value',c)
    def putdata(self):
        print('\'b\' is',self.b) 
d=demo_class() 
d.getdata(9) 
print(d.a) 
d.other_function() 
d.putdata() 
e=demo_class() 
print(e.a) 
