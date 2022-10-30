def reverse_vowels(str1):
    str1=str1.strip()
    str1.lower()
    arr=list(str1)
    vowels=['a','e','i','o','u']
    index1=0
    index2=len(str1)-1
    while index1<=index2 and index2<len(arr):
        if arr[index1] not in vowels:
           index1+=1
           continue
        if arr[index2] not in vowels:
           index2-=1
           continue
        arr[index1],arr[index2]=arr[index2],arr[index1]
        index1+=1
        index2-=1
    return ''.join(arr)

if __name__=="__main__":
   print("Reversing the vowels in a string:")
   print(reverse_vowels("hello world"))
   

        
    