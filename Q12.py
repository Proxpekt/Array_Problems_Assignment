def missing(arr, n):
    org = n * (n + 1) // 2

    return org - sum(arr)


arr = list(map(int, input().split()))
n = int(input("n: "))

print('Missing Number: ', missing(arr, n))
