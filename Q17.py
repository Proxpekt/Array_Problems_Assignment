def leaders(arr):
    n = len(arr)
    ans = []

    maxi = arr[-1]
    ans.append(maxi)

    for i in range(n - 2, -1, -1):
        if arr[i] > maxi:
            maxi = arr[i]
            ans.append(arr[i])

    ans.reverse()
    return ans


arr = list(map(int, input().split()))
print("Leader Elements:", leaders(arr))