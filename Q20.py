def rotateLeft(arr, k):
    n=len(arr)
    if n == 0:
        return arr

    k%=n

    arr[:k] = reversed(arr[:k])
    arr[k:] = reversed(arr[k:])
    arr.reverse()

    return arr

arr = list(map(int, input().split()))
k = int(input("k: "))

print("Rotated Array:", rotateLeft(arr, k))