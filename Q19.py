def subSum(arr, target):
    s = 0
    curr = 0

    for e in range(len(arr)):
        curr += arr[e]

        while curr > target and s <= e:
            curr -= arr[s]
            s += 1

        if curr == target:
            return arr[s:e + 1]

    return None


arr = list(map(int, input().split()))
target = int(input("Target: "))

ans = subSum(arr, target)
if ans:
    print("Subarray:", ans)
else:
    print("No subarray")
