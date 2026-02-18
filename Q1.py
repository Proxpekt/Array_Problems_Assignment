def rev(arr, n):
    i,j=0, n-1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return arr

arr = list(map(int,input().split()))
n = len(arr)
print(f'Reversed Array: {rev(arr, n)}')