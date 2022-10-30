def permutation(arr):
   l=list()
   def dfs(index):
      if index==len(arr):
         if arr not in l:
            l.append(arr.copy())
         return
      else:
         for i in range(0,len(arr)):
            arr[index],arr[i]=arr[i],arr[index]
            dfs(index+1)
            arr[index],arr[i]=arr[i],arr[index]
   dfs(0)
   return l

if __name__=="__main__":
   arr=[1,2,3]
   l=permutation(arr)
   print(l)
            
