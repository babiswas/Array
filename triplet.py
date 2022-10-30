def triplet0(arr):
    l=list()
    for i in range(len(arr)-2):
       for j in range(i+1,len(arr)-1):
         for k in range(j+1,len(arr)):
            sum=arr[i]+arr[j]+arr[k]
            if sum==0:
               l.append((i,j,k))
    return l


if __name__=="__main__":
   arr=[0, -1, 2, -3, 1]
   triplets=triplet0(arr)
   print(triplets)
   
