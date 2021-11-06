class Queue:
    def __init__(self,n):
        self.FRONT=-1
        self.REAR=-1
        self.a=[]
        self.n=n

    def overflow(self):
        if self.REAR==(self.n-1):
            return True
        else:
            return False

    def underflow(self):
        if self.FRONT==-1:
            return True
        else:
            return False

    def insert(self, data):
        if Queue.overflow(self):
            print('Overflow')
        elif self.FRONT==-1:
            self.FRONT=self.FRONT+1
            self.REAR=self.REAR+1     
            self.a.append(data)
            #print("Front = ",str(self.FRONT), "\tRear", str(self.REAR),"\tData\t:",str(self.a[self.REAR]))
            print("Front = ",int(self.FRONT), "\tRear", int(self.REAR),"\tData\t:",int(self.a[self.REAR]))
        
        else:
            self.REAR=self.REAR+1     
            self.a.append(data)    
            #print("Front = ",str(self.FRONT), "\tRear", str(self.REAR),"\ tData\t:",str(self.a[self.REAR]))
            print("Front = ",int(self.FRONT), "\tRear", int(self.REAR),"\ tData\t:",int(self.a[self.REAR]))

    def delete(self):
        if self.FRONT==-1:
            return (-1)
        elif self.FRONT==self.REAR:
            temp=self.a[self.FRONT]   
            print("FRONT=",self.FRONT)
            self.FRONT=-1
            self.REAR=-1
            return temp
        else:
            temp=self.a[self.FRONT]
            self.FRONT=self.FRONT+1
            print("FRONT=",self.FRONT)
            return(temp) 

q= Queue(6) 
q.insert(3) 
q.insert(2) 
q.insert(4) 
q.insert(1) 
q.insert(21) 
q.insert(71) 
i=0 
while i<6:
   temp=q.delete()   
   if temp!= -1:
       print(temp)
   else:
       print("Underflow")
   i+=1
  

