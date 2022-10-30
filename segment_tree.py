import sys
arr=[12,1,2,3,0,11,4]
seg=[0]*800

def build(index,low,high):
    if low==high:
       seg[index]=arr[low]
       return
    mid=(low+high)//2
    build(2*index+1,low,mid)
    build(2*index+2,mid+1,high)
    seg[index]=max(seg[2*index+1],seg[2*index+2])

def query(index,low,high,l,r):
    if (low>=l and high<=r):
        return seg[index]
    if low>r or high<l:
        return -sys.maxsize+1
    mid=low+((high-low)//2)
    left=query(2*index+1,low,mid,l,r)
    right=query(2*index+2,mid+1,high,l,r)
    return max(left,right)
    
def main():
   build(0,0,len(arr)-1)
   while True:
      low=input("Enter the low index")
      high=input("Enter the high index")
      print(query(0,0,len(arr)-1,int(low),int(high)))

if __name__=="__main__":
   main()
   
    
