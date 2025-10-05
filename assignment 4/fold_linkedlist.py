t = int(input())
tests = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    tests.append(arr)
results = []
for arr in tests:
    res = []
    i, j = 0, len(arr) - 1
    while i <= j:
        res.append(arr[i])
        if i != j:
            res.append(arr[j])
        i += 1
        j -= 1
    results.append(res)
for r in results:
    print(*r)
