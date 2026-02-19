def isSorted(arr):
    n=len(arr)
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False
    return True

arr=list(map(int, input().split()))
print('Array is sorted' if isSorted(arr) else 'Array is NOT sorted')