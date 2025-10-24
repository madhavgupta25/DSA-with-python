nums = [1,3,2,3,1]
left = 0
right = len(nums)-1
count = 0
while left < right:
    if nums[left] > (2*nums[right]):
        count+=1
    left+=1
    right-=1
print (count)