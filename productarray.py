def find(arr1,arr2):
    s=0
    m = len(arr2)-1
    for i in range(len(arr1)):
        s += (arr1[i]*arr2[m])
        m-=1
    return s
arr1 = [22,7,1,-5,5,-2]
arr2 = [4,-1,21,12,10,-3]
print(find(arr1,arr2))
