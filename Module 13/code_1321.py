def code():
    L = ['Harsh', 'Naved', 'Snigdha', 'Gaurav']
    try:
        index=input('Enter index\t: ')
        print(L[int(index)])
    except IndexError:
        print('List index out of bound')

code()
print('This statement always executes')
