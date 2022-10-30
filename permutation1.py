def permutation(arr):
    result=list()
    if len(arr)==1:
       return [arr.copy()]
    for i in range(len(arr)):
        n=arr.pop(0)
        l=permutation(arr)
        for sublist in l:
            sublist.append(n)
        result.extend(l)
        arr.append(n)
    return result

if __name__=="__main__":
   arr=[1,2,3]
   print(permutation(arr))

     