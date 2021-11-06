line=input('Enter a line\t:')
a=[]
rev_line='' 
words=line.split() 
print(words) 
for i in words:
   a.append(i) 
i=0 
while i<len(words):
   rev_line+=a.pop()   
   rev_line+=' '  
   i+=1 
print(rev_line)
