def pairSum(arr, target):
    n = len(arr)
    sett = set(arr)

    for num in arr:
        x = target - num

        if x in sett and x != num:
            return (num, x)

    return None

arr = list(map(int, input().split()))
target = int(input('Target: '))

ans = pairSum(arr, target)
if ans:
    print(ans)
else:
    print('No Pairs')