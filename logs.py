def find_latest(file,n):
    order=list()
    mylist=list()
    with open(file,'r') as file:
        line=file.readline()
        while len(line)!=0:
           mylist.append(line)
           line=file.readline()
        for line in mylist:
           key=line.split(' ')
           if key[1] not in order:
              order.append(key[1])
              if len(order)==n:
                 break
    for mssge in order:
        print(mssge)

if __name__=="__main__":
   file=input("Enter the filename:")
   n=input("Enter the number of message:")
   print(find_latest(file,n))
                 
           
             
 