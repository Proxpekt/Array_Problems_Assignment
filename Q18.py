def move_zeroes(arr):
    ans = []

    z0 = arr.count(0)

    for num in arr:
        if num != 0:
            ans.append(num)

    for _ in range(z0):
        ans.append(0)

    return ans


arr = list(map(int, input().split()))
print(move_zeroes(arr))
