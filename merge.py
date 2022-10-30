def merge(arr1,arr2):
   index1=0
   index2=0
   index=0
   brr=[0]*(len(arr1)+len(arr2))
   while index1<len(arr1) and index2<len(arr2):
       if arr1[index1]>arr2[index2]:
          brr[index]=arr2[index2]
          index+=1
          index2+=1
       elif arr1[index1]<arr2[index2]:
          brr[index]=arr1[index1]
          index1+=1
          index+=1
       else:
          brr[index]=arr1[index1]
          index1+=1
          index+=1
   if index1<len(arr1):
      while index1<len(arr1):
          brr[index]=arr1[index1]
          index1+=1
          index+=1
   else:
      while index2<len(arr2):
         brr[index]=arr2[index2]
         index2+=1
         index+=1
   return brr

if __name__=="__main__":
   arr1=[2,4,6,7]
   arr2=[1,3,5,8,9]
   brr=merge(arr1,arr2)
   print(brr)

          