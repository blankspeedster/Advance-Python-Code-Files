class Vector:
    def _init_(self, * args):
        self.args=args
    def putData(self):
        print(self.args)
        print('Length', Vector._len_(self))
    def _len_(self):
        self.length = len(self.args)
        return(self.length)

def _main_():
    v0= Vector()
    v0._init_()
    v0.putData()
    v1 = Vector()
    v1._init_(2)
    v1.putData()
    v2 = Vector()
    v2._init_(3, 4)
    v2.putData()
    v3 = Vector()
    v3._init_(7, 8, 9)
    v3.putData()

_main_()
