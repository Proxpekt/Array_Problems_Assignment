def remove(arr):
    seen = set()
    ans = []

    for num in arr:
        if num not in seen:
            seen.add(num)
            ans.append(num)

    return ans


arr = list(map(int, input().split()))
print(remove(arr))