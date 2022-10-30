def clear_duplicates(l):
    index=0
    count=0
    curr='@'
    while index<len(arr):
        if curr=='@':
           curr=arr[index]
           count+=1
        elif arr[index]==curr:
             count+=1
             if count>1:
                arr[index]='#'
        elif arr[index]!=curr:
            curr=arr[index]
            count=1
        index+=1
    count=len(l)
    while True:
      if '#' in l:
          l.remove('#')
      count-=1
      if count==0:
         break
    return l

if __name__=="__main__":
   arr=[1,1,2,3,4,5,5,3,4]
   arr.sort()
   l=clear_duplicates(arr)
   print(l)
   
   
       