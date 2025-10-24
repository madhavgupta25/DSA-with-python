n = int(input())
arr = [None]*n
for i in range(n):
    arr[i]=int(input())
target = int(input())
count = 0
result = []

for i in range(n):
    for j in range(i+1,n+1):
        if target == arr[i:j]:
            result.append(arr[i:j])
            count
            