        nums = 
        left = 0
        right = len(nums)-1
        count = 0
        while left < right:
            if nums[right] > (2*nums[left]):
                count+=1
        return count