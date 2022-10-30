def reverse(arr):
   index=0
   index1=len(arr)-1
   while index<index1:
       arr[index],arr[index1]=arr[index1],arr[index]
       index+=1
       index1-=1
   return arr

if __name__=="__main__":
   arr=[1,2,3,4,5,6,7]
   reverse(arr)
   print(arr)