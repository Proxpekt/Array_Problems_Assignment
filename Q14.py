def intersection(arr1, arr2):
    ans = []
    set2 = set(arr2)

    for num in arr1:
        if num in set2 and num not in ans:
            ans.append(num)

    return ans


arr1 = list(map(int, input("First array: ").split()))
arr2 = list(map(int, input("Second array: ").split()))

print(intersection(arr1, arr2))
