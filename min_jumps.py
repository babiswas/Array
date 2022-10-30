import sys
def jump(arr):
    steps=arr[0]
    jumps=0
    maxm=-sys.maxsize+1
    for i in range(len(arr)):
        steps-=1
        if maxm<arr[i]+i:
           maxm=arr[i]+i
        if steps==0:
           steps=maxm-i
           jumps+=1
    return jumps

def jumps(arr):
    def find(index):
        if index==len(arr):
           return 0
        elif arr[index]==0:
           return sys.maxsize-1
        elif arr[index]>=len(arr):
           return 1
        elif index+arr[index]>=len(arr):
           return 1
        else:
           return min([find(i) +1 for i in range(index+1,index+arr[index]+1)])
    return find(0)

if __name__=="__main__":
   arr=[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
   print("The minimum jumps to reach end of array is:")
   print(jump(arr))
   print("Second implementation:")
   print(jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
  
           
         
        