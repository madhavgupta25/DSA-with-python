nums = [1,3,2,3,1]
left = 0
right = len(nums)-1
count = 0
while left < right:
    if nums[right] > (2*nums[left]):
        count+=1
        print (count)