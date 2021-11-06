class Complex:
    def _init_(self, real=None, ima=None):
        if ((real == None)&(ima==None)):
            self.real=0
            self.ima=0
        else:
            self.real=real
            self.ima=ima

    def putData(self):
        print(str(self.real)," +i ",str(self.ima))

c1=Complex()
c1._init_(5, 3)
c1.putData()

c2=Complex()
c2._init_(None, None)
c2.putData()
