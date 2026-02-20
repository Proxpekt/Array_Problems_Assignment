def eIdx(arr):
    total = sum(arr)
    left = 0

    for i in range(len(arr)):
        total -= arr[i]

        if left == total:
            return i

        left += arr[i]

    return -1

arr = list(map(int, input().split()))
print("Equilibrim Index:", eIdx(arr))