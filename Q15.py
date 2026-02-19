def union(arr1, arr2):
    ans = []

    for num in arr1:
        if num not in ans:
            ans.append(num)

    for num in arr2:
        if num not in ans:
            ans.append(num)

    return ans


arr1 = list(map(int, input("First array: ").split()))
arr2 = list(map(int, input("Second array: ").split()))

print(union(arr1, arr2))
