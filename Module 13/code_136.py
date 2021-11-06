def findMax(L):
    max=L[0]
    for item in L:
        if item>max:
            max =item
            print('Maximum\t:',str(max))
    
L=[2, 10, 5, 89, 9] 
findMax(L) 
