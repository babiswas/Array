import heapq
def find_k_frequent(arr,K):
    m=dict()
    for i in arr:
       count=m.get(i,0)
       m.update({i:count+1})
    mylist=sorted(m.values(),reverse=True)
    print(mylist)
    d=dict()
    for key,values in m.items():
        d.update({values:key})
    index=0
    for val in mylist:
       key=d.get(val)
       print(key)
       index+=1
       if index>K:
          break

def kfrequent(arr,k):
    l=list()
    m=dict()
    for i in arr:
       count=m.get(i,0)
       m.update({i:count+1})
    heapq.heapify(l)
    for key,values in m.items():
       heapq.heappush(l,(-values,key))
    print("Processing k frequent elements:")
    while k>0:
       item=heapq.heappop(l)
       print("Frequency:",-item[0],"Value:",item[1])
       k-=1

if __name__=="__main__":
   arr=[1,1,1,2,2,3]
   find_k_frequent(arr,2)
   print("Second implementation:")
   kfrequent([1,1,1,2,2,3],3)
   
   
   
       
        