class date: 
    def getdata(self):   
        self.dd=input('Enter date (dd)\t: ')   
        self.mm=input('Enter month (mm)\t: ')   
        self.yy=input('Enter year (yy)\t: ') 
    def display(self):   
        print(self.dd,':',self.mm,':',self.yy) 
class student: 
    def getdata(self):   
        self.name=input('Enter name\t: ')   
        self.dob= date()   
        self.dob.getdata()  
    def putdata(self):   
        print('Name \t: ',self.name)   
        self.dob.display() 
s= student() 
s.getdata() 
s.putdata() 
