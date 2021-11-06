def findMax(L):
    max =L[0]
    i=1
    while i<len(L):
        if int(L[i]) > int(max):
          max = L[i]
        i+=1
    print('Maximum\t:',str(max)) 
L=[] 
item=input('Enter items (press 0 to end)\n') 
try:
    while int(item) !=0:
        L.append(item)    
        item=input('Enter item (press 0 to end)\n')
    print('\nList \n')  
    print(L)   
    findMax(L) 
except:
    print('Run time error') 
finally:
    print('This is always executed')
