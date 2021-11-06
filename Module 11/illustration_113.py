class Book:    
    def getdata(self):       
        self.name=input("\nEnter the name of the book\t: ")       
        self.n=int(input("\nEnter the number of authors\t: "))       
        self.authors=[]        
        i=0       
        while i<self.n:
            author=input(str("\nEnter the name of the "+str(i) +"th author\t: "))
            self.authors.append(author)
            i+=1       
        self.publisher=input("\nEnter the name of the publisher\t: ")       
        self.ISBN=input("\nEnter the ISBN\t: ")        
        self.year=input("\nEnter year of publication\t: ")    
    def putdata(self):        
        print("\nName\t:",self.name,"\nAuthor(s)\t:",self.  authors,"\nPublisher\t:",self.publisher,"\nYear\t:",self.year,"\nISBN\t:",self.ISBN) 
class Text_Book(Book):     
    def getdata(self):       
        self.course=input("\nEnter the course\t:")        
        Book.getdata(self)    
    def putdata(self):        
        Book.putdata(self)        
        print("\nCourse\t:",self.course) 

Book1=Book() 
Book1.getdata() 
Book1.putdata() 
TextBook1=Text_Book() 
TextBook1.getdata() 
TextBook1.putdata()
