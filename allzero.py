#move all zeros to the end of an array

def move(arr):
   index=len(arr)
   for i in range(len(arr)-1,-1,-1):
       if arr[i]==0:
          index-=1
          arr[index],arr[i]=arr[i],arr[index]
   return arr

if __name__=="__main__":
   arr=[2,3,4,0,6,8,0]
   move(arr)
   print(arr)
   
     
       
       