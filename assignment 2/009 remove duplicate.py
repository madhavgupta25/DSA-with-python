n = int(input())
arr = list(map(int, input().split()))

result = [arr[0]]  # keep first element

for i in range(1, n):
    if arr[i] != arr[i-1]:
        result.append(arr[i])

for i in result:
    print(i)
