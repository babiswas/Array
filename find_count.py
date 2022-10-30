def find_count(arr,K):
    test=1
    count=0
    for i in range(len(arr)):
       test*=arr[i]
       if test==K:
          count+=1
       if i+1<len(arr):
          for j in range(i+1,len(arr)):
              test*=arr[j]
              if test==K:
                 count+=1
          test=1
    return count


           
           
if __name__=="__main__":
   print(find_count([2, 1, 1, 1, 4, 5],4))
   

    