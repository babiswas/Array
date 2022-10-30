def trap_rain_water(arr):
    accumulate=0
    arr1=[0]*len(arr)
    arr2=[0]*len(arr)
    arr1[0]=arr[0]
    for i in range(1,len(arr)):
       if arr[i]>arr1[i-1]:
          arr1[i]=arr[i]
       else:
          arr1[i]=arr[i-1]
    arr2[len(arr)-1]=arr[len(arr)-1]
    for i in range(len(arr)-2,-1,-1):
       if arr[i]>arr2[i+1]:
         arr2[i]=arr[i]
       else:
         arr2[i]=arr2[i+1]
    for i in range(len(arr)):
       res=min(arr1[i],arr2[i])
       accumulate+=abs(res-arr[i])
    return accumulate

if __name__=="__main__":
   arr=[3,0,2,0,4]
   accumulate=trap_rain_water(arr)
   print(accumulate)
   
       
       