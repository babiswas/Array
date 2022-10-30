def find(arr,index):
    if index>=len(arr):
       return 0
    return max(find(arr,index+2)+arr[index],find(arr,index+2))
if __name__=="__main__":
   arr=[5, 5, 10, 100, 10, 5]
   num=find(arr,0)
   print(num)

   
   
   