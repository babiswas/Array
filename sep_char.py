def sep_char(l):
   index=-1
   for i in range(len(l)):
     if l[i]=='b':
        index+=1
        l[index],l[i]=l[i],l[index]
   for i in range(index+1,len(l)):
      if l[i]=='w':
         index+=1
         l[index],l[i]=l[i],l[index]
   for i in range(index+1,len(l)):
      if l[i]=='r':
         index+=1
         l[index],l[i]=l[i],l[index]
   return l

if __name__=="__main__":
   l=['r','w','b','b','w','r','b','w','r','b']
   print(sep_char(l))
   
   
        