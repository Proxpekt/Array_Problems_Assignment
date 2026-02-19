def rotate(arr, k):
    n=len(arr)
    k%=n

    arr.reverse()
    arr[:k] = reversed(arr[:k])
    arr[k:] = reversed(arr[k:])

    return arr

arr = list(map(int, input().split()))
k = int(input("k: "))

print("Rotated Array:", rotate(arr, k))