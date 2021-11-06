class Data:
    def __len__(self):
        return 0

X = Data()
if X:
    print("True returned")
else:
    print("False returned")
