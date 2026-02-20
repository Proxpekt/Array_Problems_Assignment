def sort012(arr):
    l = 0
    mid = 0
    r = len(arr) - 1

    while mid <= r:
        if arr[mid] == 0:
            arr[l], arr[mid] = arr[mid], arr[l]
            l += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[r] = arr[r], arr[mid]
            r -= 1

    return arr


arr = list(map(int, input().split()))
print("Sorted Array:", sort012(arr))