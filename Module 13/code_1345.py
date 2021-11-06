class MyError (Exception):
    def _init__():
        print('My Error type error')
    
    def divide(a, b):
        try:
            if b==0:
                raise MyError
            d=a/b
            print('Result is\t:',str(d))
        except MyError:
            print('Exception caught : MyError ')

MyError.divide(2,3)
MyError.divide(2,0) 
