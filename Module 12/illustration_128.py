class Data:
    def __init__(self, value):
        self.value = value

    def __len__(self):
        if len(self.value) == 0:
            return 0
        else:
            return 1

    def __bool__(self):
        if len(self.value) == 0:
            print("From Bool")
            return False
        else:
            print("From Bool")
            return True

Y = Data("hi")
if Y:
    print("True returned")
else:
    print("False returned")
X = Data("")
if X:
    print("True returned")
else:
    print("False returned")
