def count_subarr_kproduct(arr,K):
    test=1
    index1=0
    index2=0
    count1=0
    count=0
    while index1<=index2 and index2<len(arr):
         test*=arr[index2]
         if test>K:
            while test>K:
               test=test//arr[index1]
               index1+=1
         if test==K:
            while index2+1<len(arr) and arr[index2+1]==1:
                  count1+=1
                  index2+=1
            count+=count1+1
            while arr[index1]==1 and index1<=index2 and K!=1:
                  count+=count1+1
                  index1+=1
            test=test//arr[index1]
            index1+=1
         index2+=1
    return count

if __name__=="__main__":
   arr=[2, 1, 1, 1, 4, 5]
   print(count_subarr_kproduct(arr,4))
   
   
            
            
