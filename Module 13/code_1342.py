def divide(a, b):
    try:
        if b==0:
            raise ZeroDivisionError
        d=a/b  
        print('Result is\t:',str(d))
    except ZeroDivisionError :
        print('Exception caught:ZeroDivisionError ')

divide(2,3)
divide(2,0)
