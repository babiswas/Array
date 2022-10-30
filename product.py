def find_product(arr,k):
   prod=1
   for i in range(len(arr)):
      prod*=arr[i]
   if k>=0 and k<len(arr):
      return prod//arr[k]
   else:
      return -1

if __name__=="__main__":
   arr=[10, 3, 5, 6, 2]
   print(find_product(arr,3))
   
   