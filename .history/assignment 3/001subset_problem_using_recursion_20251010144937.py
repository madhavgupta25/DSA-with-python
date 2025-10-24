n = int(input())
arr = [None]*n
for i in range(n):
    arr[i]=int(input())
target = int(input())

for i in range(n):
    for j in range(i+1,n+1):
        if target == arr[i]