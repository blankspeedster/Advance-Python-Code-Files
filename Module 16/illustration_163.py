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

class Queue:  

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

    def enqueue(self, val): 
        tempNode=Node()   
        tempNode.setVal(val)  
        current=self.head   
        if current!=None: 
            while current.getNext()!=None: 
                current=current.link   
                current.link=tempNode  
                tempNode.link=None  
                self.length+=1  
        else:   
            self.head=tempNode  
            self.length=self.length+1 

    def dequeue(self):   
        current=self.head   
        if current!=None:  
            current=self.head  
            next1=current.link  
            self.head=next1     
            self.length=self.length-1 
        else:   
            print('Cannot delete')

    def traverse(self):
        current=self.head
        while current!=None:
            print(current.data,end=" ") 
            current=current.getNext()

Q = Queue()
print('\nQueue') 
Q.traverse()
Q.enqueue(2) 
print('\nQueue')
Q.traverse()
#[2]
Q.enqueue(5) 
print('\nQueue')
Q.traverse()
#[2,5]
Q.enqueue(7)
print('\nQueue');
Q.traverse()
#[2,5,7]
Q.dequeue()
print('\nQueue');
Q.traverse() 
#[5,7]
Q.dequeue()
print('\nQueue');
Q.traverse() 
#[7]
