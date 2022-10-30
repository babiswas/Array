def find_subset(arr1,arr2):
    for i in range(len(arr1)):
      for j in range(len(arr2)):
          if arr1[i]==arr2[j]:
             break
      if j==len(arr2):
        return False
    return True

def find_subset(arr1,arr2):
    def bsearch(arr,low,high,key):
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==key:
               return mid
            elif arr[mid]>key:
                high=mid-1
            elif arr[mid]<key:
                low=mid+1
        return -1
    arr2.sort()
    for i in arr1:
        index=bsearch(arr2,0,len(arr2)-1,i)
        if index==-1:
           return False
    return True
        
    

if __name__=="__main__":
   arr1=[11, 3, 7, 1]
   arr2=[11, 1, 13, 21, 3, 7]
   print(find_subset(arr1,arr2))
   print("Find subset using 2nd implementation:")
   print(find_subset(arr1,arr2))
   
