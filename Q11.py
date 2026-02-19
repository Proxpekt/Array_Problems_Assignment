def removeEle(arr, x):
    ans = []
    for num in arr:
        if num != x:
            ans.append(num)
    return ans


arr = list(map(int, input().split()))
x = int(input("Element: "))

print(removeEle(arr, x))