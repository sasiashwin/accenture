def find(arr):
    n = 0
    s = 0
    for i in range(len(arr)-1,-1,-1):
        if(arr[i]>n):
            s+=arr[i]
            n = arr[i]
    return s
arr = [33,7,21,14]
print(find(arr))
