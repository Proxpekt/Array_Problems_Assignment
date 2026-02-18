def secondLargest(arr):
    maxi = float('-inf')
    second = float('-inf')

    for num in arr:
        if num > maxi:
            second = maxi
            maxi = num
        elif num > second and num != maxi:
            second = num

    return second

arr = list(map(int, input().split()))
print(f'Second maximum element is: {secondLargest(arr)}')