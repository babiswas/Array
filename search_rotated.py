def search_rotated(arr,target):
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
           return mid
        if arr[mid]>arr[low]:
           if target>arr[mid] or target<arr[low]:
              low=mid+1
           else:
              high=mid-1
        else:
           if target<arr[mid] or target>arr[high]:
              high=mid-1
           else:
              low=mid+1
             
    return -1

if __name__=="__main__":
  arr=[5,6,7,1,2,3]
  for i in arr:
    print(search_rotated(arr,i))
   
           