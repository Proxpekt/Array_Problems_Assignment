from collections import Counter

def equal(arr1, arr2):
    freq = Counter(arr1)

    for num in arr2:
        if num not in freq or freq[num] == 0:
            return False
        freq[num] -= 1

    return True


arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

print("Equal" if equal(arr1, arr2) else "NOT equal")