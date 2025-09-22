n = int(input())
arr = [int(input()) for _ in range(n)]
for i in range(n-1, -1, -1):
    print(str(arr[i]) + " ", end="")