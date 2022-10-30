def filter_char(arr):
   count=0
   index=0
   curr='$'
   while index<len(arr):
       if curr=='$':
          curr=arr[index]
          count+=1
       elif arr[index]==curr and count!=0:
            count+=1
            if count>2:
               arr[index]='#'
       elif arr[index]!=curr:
            count=1
            curr=arr[index]
       index+=1
   print(arr)
   count=len(arr)
   while True:
      if '#' in arr:
        arr.remove('#')
      count-=1
      if count==0:
         break
   return len(arr)

if __name__=="__main__":
   arr=[0,0,1,1,1,1,2,3,3]
   print(filter_char(arr))
   print(arr)
   
   

        
            
       