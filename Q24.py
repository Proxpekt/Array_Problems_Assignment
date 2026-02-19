def rearrange(arr):
    arr.sort()
    ans = []

    i = 0
    j = len(arr) - 1

    while i <= j:
        if i != j:
            ans.append(arr[j])
            ans.append(arr[i])
        else:
            ans.append(arr[i])
        i += 1
        j -= 1

    return ans


arr = list(map(int, input().split()))
print(f"Rearranged Array: {rearrange(arr)}")