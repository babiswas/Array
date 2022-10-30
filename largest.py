import sys
def find_second_large(arr):
    maxm=-sys.maxsize+1
    maxm1=-sys.maxsize+1
    index=0
    while index<len(arr):
        if arr[index]>maxm:
           maxm1=maxm
           maxm=arr[index]
        else:
           if arr[index]>maxm1:
              maxm1=arr[index]
        index+=1

    return maxm1

if __name__=="__main__":
   arr=[11,10,12,19,4,20,16]
   print(find_second_large(arr))
   