def majority(arr):
    n=len(arr)
    count = 0
    ans = None

    for num in arr:
        if count == 0:
            ans = num
        count += 1 if num == ans else -1

    if arr.count(ans) > n // 2:
        return ans
    return None


arr = list(map(int, input().split()))
result = majority(arr)

if result is not None:
    print(f"Majority Element: {result}")
else:
    print("No Majority Element")
