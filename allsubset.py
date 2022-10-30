def find_all_subset(arr):
    l=list()
    temp=list()
    def find(index):
        if index==len(arr):
           if len(temp)==3:
              l.append(temp.copy())
           return 
        temp.append(arr[index])
        find(index+1)
        temp.pop()
        find(index+1)
    find(0)
    return l

if __name__=="__main__":
   arr=[1,2,3,4]
   m=find_all_subset(arr)
   print(m)

   
   
    
        