def find(arr1,arr2,target):
    for i in arr1:
       for j in arr2:
          if i+j==target:
             print(i,j)

def findpair(arr1,arr2,target):
    arr1.sort()
    arr2.sort()
    def bsearch(arr,low,high,key):
       while low<=high:
            mid=(low+high)//2
            if arr[mid]==key:
               return mid
            if arr[mid]<key:
               low=mid+1
            else:
               high=mid-1
       return -1
    for i in arr1:
       item=target-i
       key=bsearch(arr2,0,len(arr2)-1,item)
       if key!=-1:
         print(i,arr2[key])

def findpair2(arr1,arr2,target):
    m=dict()
    for index,value in enumerate(arr1):
        m.update({value:index})
    for i in arr2:
       item=target-i
       key=m.get(item,-1)
       if key!=-1:
          print(i,item)
          

if __name__=="__main__":
   arr1=[1, 2, 4, 5, 7]
   arr2=[5, 6, 3, 4, 8]
   find(arr1,arr2,9)
   print("=====================")
   print("Second implementation:")
   findpair(arr1,arr2,9)
   print("======================")
   print("Third implementation:")
   findpair2(arr1,arr2,9)
   
   
   
   
      