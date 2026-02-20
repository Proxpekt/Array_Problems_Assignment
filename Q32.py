def maxProd(arr):
    arr.sort()
    n = len(arr)

    p1 = arr[0] * arr[1]          
    p2 = arr[n-1] * arr[n-2]      

    if p1 > p2:
        return (arr[0], arr[1])
    else:
        return (arr[n-2], arr[n-1])

arr = list(map(int, input().split()))
print("Pair:", maxProd(arr))