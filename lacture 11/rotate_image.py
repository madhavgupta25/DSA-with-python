nums = [[11, 12 ,13 ,14], 
        [21, 22 ,23 ,24], 
        [31, 32 ,33 ,34], 
        [41, 42 ,43 ,44]]
n = len(nums)
for i in range(n):
    for j in range(i+1, n):
        nums[i][j], nums[j][i] = nums[j][i], nums[i][j]
    
for row in nums:
    row.reverse()

for i in range(n):
    for j in range(n):
        print(nums[i][j], end=" ")
    print("")  # for new line