n = int(input("enter the size of array : ").strip())
arr = [int(input().strip()) for _ in range(n)]
count_zeros = 0
for i in arr:
    if i == 0:
        count_zeros+=1

abc = "0" * count_zeros+"1"*(n-count_zeros)
print(*abc)