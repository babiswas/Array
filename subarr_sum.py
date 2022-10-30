def subarr_sum(arr,target):
    index1=0
    index2=0
    sum=0
    while index1<=index2 and index2<len(arr):
        sum+=arr[index2]
        if sum>target:
           while sum>target:
              sum-=arr[index1]
              index1+=1
        if sum==target:
            return index1,index2
        index2+=1
    return -1,-1

if __name__=="__main__":
   arr=[1, 4, 20, 3, 10, 5]
   index1,index2=subarr_sum(arr,33)
   print(arr[index1:index2+1])
   print(index1,index2)

   
   