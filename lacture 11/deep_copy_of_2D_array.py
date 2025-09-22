import copy
nums =[[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
nums_copy = copy.deepcopy(nums)
print("Original array:")
print(nums)
print("Deep copied array:")
print(nums_copy)
nums_copy[0][0] = 100
print(nums_copy)
print("After modifying the copy, original array remains unchanged:")
print(nums)
