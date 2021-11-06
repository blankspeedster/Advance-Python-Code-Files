class Complex:
    def _init_(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def putData(self):
        print(self.real," + i ",self.imaginary)

def _main_():
    c1=Complex()
    c1._init_(5, 3)
    c1.putData()

_main_()
