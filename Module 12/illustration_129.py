class Data:
    def __init__(self, value):
        self.value = value

    def __len__(self):
        if len(self.value) == 0:
            return 0
        else:
            return 1

# X= Data()
# if X:
# print("True returned")
# else:
# print("False returned")
Y = Data("hi")
if Y:
    print("True returned")
else:
    print("False returned")
X = Data("")
if X:
    print("Ture returned")
else:
    print("False returned")
