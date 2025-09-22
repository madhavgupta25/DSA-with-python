def is_present(nums:list[list[int]], target:int) -> bool:
    m = len(nums)
    n = len(nums[0])

    i=0
    j=n-1
    while i<= m-1 and j>= 0:
        if nums[i][j] == target:
            return True
        elif nums[i][j] < target:
            i += 1
        else:
            j -= 1
    return False

nums = [[10, 20 ,30 ,40], 
        [50, 60 ,70 ,80], 
        [70, 80 ,90 ,100], 
        [110, 120 ,130 ,140]]
target = 140
print(is_present(nums, target))

