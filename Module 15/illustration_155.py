str= input('Enter a string\t: ') 
rev_string='' 
a=[] 
for i in str:
   a.append(i) 
i=0 
while i<len(str):
   x=a.pop()   
   rev_string=rev_string+ x   
   i=i+1 
   
print(rev_string)
