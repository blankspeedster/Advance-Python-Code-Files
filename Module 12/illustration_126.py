class Data:
    def __init__(self, value):
        self.value = value

    def display(self):
        print("data is ", str(value))

    def __lt__(self, other):
        return(self.value < other.value)

    def __gt__(self, other):
        return(self.value > other.value)

X = Data(5)
Y = Data(4)
print(X < Y)
