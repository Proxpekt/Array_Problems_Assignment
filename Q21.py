def kSmallest(arr, k):
    arr.sort()
    return arr[k-1]


arr = list(map(int, input().split()))
k = int(input("k: "))

print(f'kth Smallest Element: {kSmallest(arr, k)}')