li=list(range(1,8))

def rotate(arr):
    first=arr[0]
    for x in range(len(arr)-1): #O(N)
        arr[x]=arr[x+1]
    arr[-1]=first

def rotate_n(arr,n): # O(N*n)
    for x in range(0,n):
        rotate(arr)
        
rotate_n(li,3)        
    
print(li)