n = int(input())
arr = list(map(int, input().split()))
result=[0]*n
for i in range(0,n):
    result[i] = arr[i]*arr[i]

result.sort()
for i in result:
    print(i)

print(*result)
