def maxDiff(arr):
    mini = arr[0]
    maxi = arr[1] - arr[0]

    for i in range(1, len(arr)):
        if arr[i] - mini > maxi:
            maxi = arr[i] - mini

        if arr[i] < mini:
            mini = arr[i]

    return maxi

arr = list(map(int, input().split()))
print("Maximum Difference:", maxDiff(arr))