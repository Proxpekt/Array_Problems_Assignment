def subarrays(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            print(arr[i:j+1])


arr = list(map(int, input().split()))
subarrays(arr)