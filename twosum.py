def find(arr,target):
    arr.sort()
    index1=0
    index2=len(arr)-1
    while index1<index2:
        diff=target-arr[index1]
        if diff>arr[index2]:
           index1+=1
        elif diff<arr[index2]:
           index2-=1
        else:
           return index1,index2
    return -1,-1

def find_target(arr,target):
    m=dict()
    for index,value in enumerate(arr):
        m.update({value:index})
    for i in range(len(arr)):
        diff=target-arr[i]
        index=m.get(diff,-1)
        if index!=-1:
           if index!=i:
              return index,i
           else:
              continue
    return -1,-1

if __name__=="__main__":
   arr=[0, -1, 2, -3, 1]
   index1,index2=find(arr,-2)
   print(index1,index2)
   print(arr[index1],arr[index2])
   print("Second implementation")
   index1,index2=find_target(arr,-2)
   print(arr[index1],arr[index2])
   
    
    