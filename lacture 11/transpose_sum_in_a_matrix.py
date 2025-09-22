nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]
m = len(nums)
n = len(nums[0])
def matrixSum(nums: list[list[int]]) -> int:
    # Sort each row ascending
    for row in nums:
        row.sort()
    
    total = 0
    # Loop over columns
    for col in range(n):  # assume all rows same length
        max_val = 0
        for row in nums:
            max_val = max(max_val, row[col])
        total += max_val
    return total