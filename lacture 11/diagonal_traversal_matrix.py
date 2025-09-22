def print_diagonal(nums:list[list[int]] , i:int , j:int)->None:
    m = len(nums)
    n = len(nums[0])

    while i<= m-1 and j<= n-1:
        print(nums[i][j], end=" ")
        i += 1
        j += 1
    # print()



nums = [[11, 12 ,13 ,14], 
        [15, 16 ,17 ,18],  
        [19, 20 ,21 ,22]]
m = len(nums)
n = len(nums[0])

for j in range(n):
    print_diagonal(nums , 0 , j)

for i in range(1, m):
    print_diagonal(nums , i , 0)

print()
print("sir wala output")
# Output

for i in range(2 , 0, -1):
    print_diagonal(nums , i , 0)

for j in range(n):
    print_diagonal(nums , 0 , j)