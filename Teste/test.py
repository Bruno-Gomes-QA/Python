
def two_sum(arr, target):
    hasher = {}
    for i, n in enumerate(arr):
        diff = target-n 
        hasher[diff] = i
        print(hasher)
        rest = hasher.get(n)
        if rest is not None:
            return [i, rest]

arr = [11, 15, 7, 2, 4, 8]
target = 15

result = two_sum(arr, target)
print(result)