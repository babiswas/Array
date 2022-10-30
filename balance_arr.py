def balance(arr):
    even_sum=sum([arr[i] for i in range(0,len(arr),2)])
    odd_sum=sum([arr[i] for i in range(1,len(arr),2)])
    if odd_sum==even_sum:
       return -1
    index=0
    ce_sum=0
    co_sum=0
    while index<len(arr):
       if index%2==0:
          if even_sum-ce_sum-arr[index]+co_sum==odd_sum-co_sum+ce_sum:
             return index
          ce_sum+=arr[index]
       else:
          if even_sum-ce_sum+co_sum==odd_sum-arr[index]-co_sum+ce_sum:
             return index
          co_sum+=arr[index]
       index+=1
    return -1

if __name__=="__main__":
   arr=[ 2, 1, 6, 4]
   print(balance(arr))
    