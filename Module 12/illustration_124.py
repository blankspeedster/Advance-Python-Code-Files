##fractions
class fraction:
    def __init__(self):
        self.num=0;
        self.den=1;
    def getdata(self):
        self.num=input("Enter the numerator\t:")
        self.den = input("Enter the denominator\t:")
    def display(self):
        print(str(int(self.num)),"/",str(int(self.den)))
    def gcd(first, second):
        if(first<second):
            temp=first
            first=second
            second=temp
        if(first%second==0):
            return second
        else:
            return(fraction.gcd(second, first%second))
            def lcm(first, second):
                ##print("GCD is",str(fraction.gcd(first,second)))
                return((first*second)/fraction.gcd(first,second))
    def _add_(self,other):
        s=fraction()
        lc=fraction.lcm(int(self.den), int(other.den))
        s.num=((lc/int(self.den))*int(self.num))+((lc/int(other.den))*int(other.num))
        s.den=lc
        return(s)
    def _sub_(self,other):
        lc=fraction.lcm(int(self.den), int(other.den))
        d=fraction()
        d.num=((lc/int(self.den))*int(self.num))-((lc/int(other.den))*int(other.num))
        d.den=lc
        return(d)
    def _mul_(self,other):
        m=fraction()
        m.num=int(self.num)*int(other.num)
        m.den=int(self.den)*int(other.den)
        return(m)
    def __truediv__(self,other):
        answer=fraction()
        answer.num=int(self.num)*int(other.den)
        answer.den=int(self.den)*int(other.num)
        return(answer)
x =fraction()
x.getdata()
print("First fraction\t:")
x.display()
y=fraction()
y.getdata()
print("Second fraction\t:")
y.display()
z=(x+y)
print("Sum\t:")
z.display()
t=x-y
print("Difference\t:")
t.display()
prod=x*y
print("Product")
prod.display()
div=x/y
print("Division")
div.display()

