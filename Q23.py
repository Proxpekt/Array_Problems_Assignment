def kadanes(arr):
    maxi = arr[0]
    curr = arr[0]

    for i in range(1, len(arr)):
        curr = max(arr[i], curr + arr[i])
        maxi = max(maxi, curr)

    return maxi


arr = list(map(int, input().split()))
print(f"Maximum Subarray Sum: {kadanes(arr)}")