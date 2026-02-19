from collections import Counter

arr = list(map(int, input().split()))

c = Counter(arr)
ans = [key for key, val in c.items() if val > 1]

if ans:
    print("Duplicate elements:", ans)
else:
    print("No duplicates found")
