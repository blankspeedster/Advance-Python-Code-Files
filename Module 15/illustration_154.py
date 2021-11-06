class Stack:
    def __init__(self,n):
        self.TOP=-1
        self.a=[]
        self.n=2*n

    
    def check(self):
        if self.TOP==(self.n-1):
            self.resize()

    def underflow(self):
        if self.TOP==-1:
            return True
        else:
            return False

    def push(self, data):
        Stack.check(self)
        self.TOP=self.TOP+1
        self.a.append(data)
        print("TOP =",self.TOP)

    def pop(self):
        if Stack.underflow(self):
            print("Underflow...")
            return (-1)
        else:
            temp=self.a.pop()
            self.TOP=self.TOP-1
            print("TOP=",self.TOP)
            return(temp)

    def resize(self):
        self.n=self.n+1
