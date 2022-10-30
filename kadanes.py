import sys
def kadanes(arr):
   sum=0
   index1=0
   index2=0
   maxm=-sys.maxsize+1
   for i in range(len(arr)):
      sum+=arr[i]
      if sum>maxm:
         maxm=sum
         index2=i
         index1=index1
      if sum<0:
         sum=0
         index1=i+1
   return index1,index2

if __name__=="__main__":
   arr=[-2, -3, 4, -1, -2, 1, 5, -3]
   index,index1=kadanes(arr)
   print(index,index1)
   print(sum(arr[index:index1+1]))
   
        