def rotate(arr,k):
    num=k%len(arr)
    for i in range(num):
        arr[i],arr[len(arr)-1-i]=arr[len(arr)-1-i],arr[i]
    index=0
    index1=num-1
    while index<=index1:
        arr[index],arr[index1]=arr[index1],arr[index]
        index+=1
        index1-=1
    index=len(arr)-1
    index1=num
    while index1<index:
       arr[index1],arr[index]=arr[index],arr[index1]
       index-=1
       index1+=1
    return arr

if __name__=="__main__":
   print("The rotated array is:")
   arr=[1,2,3,4,5,6,7]
   print(rotate(arr,3))
    