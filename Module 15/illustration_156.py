Insert(item)
  {  
if( REAR == (n-1)):
        {
       print ("overflow");
        } 
else       
        {       
        if(FRONT == -1)
            {
            FRONT = REAR = 0;            
            a[REAR] =item;            
            }       
        else            
            {            
            REAR = REAR +1;            
            a[REAR] = item;            
            }       
        } 
  } 
