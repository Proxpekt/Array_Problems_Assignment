from collections import Counter

arr = list(map(int, input().split()))
freq = Counter(arr)

print('Element Frequencies:')
for key, val in freq.items():
    print(f'{key}: {val}')