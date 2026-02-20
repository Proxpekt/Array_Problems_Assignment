def prod(arr):
    n = len(arr)
    ans = [1] * n

    pre = 1
    for i in range(n):
        ans[i] = pre
        pre *= arr[i]

    suff = 1
    for i in range(n-1, -1, -1):
        ans[i] *= suff
        suff *= arr[i]

    return ans

arr = list(map(int, input().split()))
print("Product Array:", prod(arr))