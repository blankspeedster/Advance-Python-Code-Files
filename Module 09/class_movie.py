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
m=movie()
m.getdata()
m.putdata()
