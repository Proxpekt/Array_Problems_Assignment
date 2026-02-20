def missing(arr):
    n = len(arr)

    for i in range(n):
        if arr[i] <= 0 or arr[i] > n:
            arr[i] = n + 1

    for i in range(n):
        num = abs(arr[i])
        if 1 <= num <= n:
            arr[num - 1] = -abs(arr[num - 1])

    for i in range(n):
        if arr[i] > 0:
            return i + 1

    return n + 1


arr = list(map(int, input().split()))
print("First Missing:", missing(arr))