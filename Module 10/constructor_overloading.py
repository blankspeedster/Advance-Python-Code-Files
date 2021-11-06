class movie: 
    def getdata(self):   
        self.name=input('Enter name\t: ')   
        self.year=int(input('Enter year\t: '))   
        self.genre=input('Enter genre\t: ')  
        self.director=input('Enter the name of the director\t: ')  
        self.producer=input('Enter the producer\t: ')  
        L=[]  
        item=input('Enter the name of the actor\t: ')   
        L.append(item)  
        choice=input('Press \'y\' for more \'n\' to quit ')   
        while(choice == "y"):   
            item=input('Enter the name of the actor\t: ')    
            L.append(item)   
            choice=input('Enter \'y\' for more \'n\' to quit ')   
        self.actors=L  
        self.music_director=input('Enter the name of the music director\t: ') 
    def putdata(self):   
        print('Name\t:',self.name)   
        print('Year\t',self.year)   
        print('Genre\t:',self.genre)   
        print('Director\t:',self.director)   
        print('Producer\t:',self.producer)  
        print('Music_director\t:',self.music_director)   
        print('Actors\t:',self.actors) 
    def init (self):   
        self.name='Fault'   
        self.year=2015   
        self.genre='Drama'   
        self.director='XYZ'   
        self.producer='ABC'   
        self.music_director='LMN'  
        self.actors=['A1', 'A2', 'A3', 'A4'] 
m=movie()
m.init()
#m.getdata()
m.putdata() 
