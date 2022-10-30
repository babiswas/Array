def min_swaps(l):
   index=-1
   swap=0
   for i in range(len(l)):
       if l[i]==0:
          index+=1
          l[index],l[i]=l[i],l[index]
          swap+=1
   print(l)
   return swap

if __name__=="__main__":
   l=[1,0,1,0,1]
   print(min_swaps(l))