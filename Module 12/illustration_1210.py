class Data:
    def _init_(self, value):
        self.value=value
    def display(self):
        print("Value\t:",str(self.value))
    def _del_(self):
        print("Destructor called")
X=Data()
X._init_(5)
X.display()
X._del_()
