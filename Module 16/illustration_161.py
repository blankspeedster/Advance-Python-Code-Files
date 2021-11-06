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

class LinkedList:

    def __init__(self):
        self.head=None
        self.length=0

    def listLength(self):
        current=self.head
        count=0
        while current!=None:
            count=count+1
            current=current.getNext()
        return count  

    def insertBeg(self,val):     
        tempNode=Node()     
        tempNode.setVal(val)
        if self.length==0:
            self.head=tempNode
        else:
            tempNode.setNext(self.head)
            self.head=tempNode
            self.length+=1  

    def insertEnd(self, val):
        tempNode=Node()
        tempNode.setVal(val)      
        current=self.head      
        while current.getNext()!=None:              
            current=current.getNext()              
            current.setNext(tempNode)         
        self.length+=1  

    def insertAfter(self, val1, val):
        tempNode=Node()    
        tempNode.setVal(val)     
        current=self.head    
        while current.data!=val1:
            current=current.getNext()    
            current1=current.getNext()     
            current.setNext(tempNode)     
            tempNode.setNext(current1)  

    def del_beg(self):
        current=self.head     
        if current!=None:
            current=self.head       
            next1=current.link       
            self.head=next1       
            self.length=self.length-1
        else:
            print('Cannot delete')  

    def del_end(self):     
        current=self.head     
        if current!=None:      
            while (current.link).link!=None:           
                current=current.link       
                current.link=None     
        else:       
            print('Cannot delete')

    def del_after(self, val):     
        flag=0    
        current=self.head
        while current.data!=val:
            current=current.link    
            current1=current.link     
            current2=current1.link     
            current.link=current2     
            self.length=self.length-1  

    def clear(self):     
        self.head=None  

    def traverse(self):     
        current=self.head     
        while current!=None:      
            print(current.data,end=" ")       
            current=current.getNext() 

L = LinkedList() 
print('\nList'); 
L.traverse() 
L.insertBeg(2) 
print('\nList'); 
L.traverse() 
L.insertBeg(5) 
print('\nList'); 
L.traverse() 
L.insertBeg(7) 
print('\nList'); 
L.traverse() 
L.insertAfter(5,8) 
print('\nList') 
L.traverse() 
L.insertEnd(9) 
print('\nList') 
L.traverse() 
print('\nLength\t',str(L.listLength())) 
L.del_beg() 
print('\nList') 
L.traverse() 
L.del_after(8) 
print('\nList')
L.traverse() 
L.del_end() 
print('\nList') 
L.traverse() 
L.clear() 
print('\nList'); 
L.traverse() 
L.del_beg() 
L.traverse()
