class Node:
    def __init__(self):
        self.data=None
        self.link=None

    def setVal(self, val):
        self.data=val

    def getVal(self):
        return self.data

    def setNext(self, next1):
        self.link=next1

    def getNext(self):  
        return self.link 

    def hasNext(self):
        if self.link!=None:
            return True
        else:     
            return False 

class Stack:
    def __init__(self):
        self.head=None
        self.length=0
        
    def Length(self):  
        current=self.head
        count=0 
        while current!=None:
            count=count+1     
            current=current.getNext()   
            return count  

    def push(self, val):
        tempNode=Node() 
        tempNode.setVal(val)  
        current=self.head    
        if current!=None: 
            while current.getNext()!=None:   
                current=current.getNext()   
            current.setNext(tempNode)   
            self.length+=1   
        else: 
            self.head=tempNode 

    def pop(self):    
        current=self.head   
        if current!=None:
            while (current.link).link!=None:
                current=current.link 
                data=current.data 
                current.link=None  
        else:      
            print('Underflow')    
            data=-1  
            return data 

    def traverse(self): 
        current=self.head  
        while current!=None:    
            print(current.data,end=" ")    
            current=current.getNext() 

S = Stack() 
print('\nStack') 
S.traverse() 
S.push(2) 
print('\nStack') 
S.traverse() 
#[2] 
S.push(5) 
print('\nStack'); 
S.traverse() 
#[2,5] 
S.push(3) 
print('\nStack'); 
S.traverse() 
#[2,5,3] 
val=S.pop() 
if val!=-1:   
    print('\n',str(val), 'popped') 
print('\nStack') 
S.traverse() 
#[2,5] 
val=S.pop() 
if val!=-1: 
    print('\n',str(val), 'popped') 
print('\nStack') 
S.traverse() 
#[2]
