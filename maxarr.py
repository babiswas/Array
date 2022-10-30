def max_sum(arr):
   def func(index):
       if index>=len(arr):
          return 0
       else:
          return max(func(index+2)+arr[index],func(index+1))
   return func(0)

if __name__=="__main__":
  arr=[5, 5, 10, 100, 10, 5]
  print(max_sum(arr))
  brr=[3, 2, 7, 10]
  print(max_sum(brr))
  crr=[3, 2, 5, 10, 7]
  print(max_sum(crr))
  print("=====================")
  brr=[3, 2, 7, 10]
  print(find_maxm(brr))
   
      
          