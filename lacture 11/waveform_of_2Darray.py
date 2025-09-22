m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
nums = [[None] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        nums[i][j] = int(input())

for j in range(n):
    if j%2 == 0:
        for i in range(n):
            print(nums[i][j], end=" ")
    else:
        for i in range(n-1, -1, -1):
            print(nums[i][j], end=" ")