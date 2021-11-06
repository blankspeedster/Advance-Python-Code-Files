# overloading += for Complex class
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __iadd__(self, other):
        self.real += other.real
        self.imaginary += other.imaginary
        return self

    def display(self):
        print("Real part\t:", str(self.real), " Imaginary part\t:", str(self.imaginary))

X = Complex(2, 3)
Y = Complex(4, 5)
X.display()
Y.display()
X += Y
X.display()
X += Y
X.display()
