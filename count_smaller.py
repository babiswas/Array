import heapq
def count_smaller(arr):
    brr=[0]*len(arr)
    count=0
    for i in range(len(arr)-1):
      for j in range(i+1,len(arr)):
         if arr[i]>arr[j]:
            count+=1
      brr[i]=count
      count=0
    return brr

def count_smaller2(arr):
    mylist=list()
    count=0
    l=list()
    heapq.heapify(l)
    for i in range(len(arr)):
       heapq.heappush(l,arr[i])
    index=len(arr)
    while index!=0:
       q=heapq.heappop(l)
       mylist.append((q,count))
       count+=1
       index-=1
    print(mylist)
    
        
    

if __name__=="__main__":
   print("==========================")
   arr=[12, 1, 2, 3, 0, 11, 4]
   brr=count_smaller(arr)
   print(brr)
   print("==========================")
   print("Second implementation:")
   count_smaller2(arr)
   print("==========================")

   
         
    