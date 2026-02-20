def peek(arr):
    n = len(arr)

    for i in range(n):
        if (i == 0 or arr[i] > arr[i-1]) and (i == n-1 or arr[i] > arr[i+1]):
            return arr[i]

    return None

arr = list(map(int, input().split()))
print("Peak Element:", peek(arr))