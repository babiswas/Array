def find_minm(arr):
    l,r=0,len(arr)-1
    res=arr[0]
    while l<=r:
       if arr[l]<arr[r]:
          res=min(res,arr[l])
          break
       mid=(l+r)//2
       res=min(res,arr[mid])
       if arr[mid]>arr[l]:
          l=mid+1
       else:
          r=mid-1
    return res

if __name__=="__main__":
   arr=[10,11,12,6,7,8,9]
   print(find_minm(arr))
