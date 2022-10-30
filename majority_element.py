def majority_element(arr):
    count=0
    curr=arr[0]
    for i in range(1,len(arr)):
       if arr[i]==curr:
          count+=1
       else:
          count-=1
       if count<0:
          curr=arr[i]
          count=1
    count=0
    for i in range(len(arr)):
      if arr[i]==curr:
         count+=1
    print(curr,count)

if __name__=="__main__":
   arr=[3, 3, 4, 2, 4, 4, 2, 4, 4]
   majority_element(arr)
   

      