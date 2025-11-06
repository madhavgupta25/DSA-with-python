class Solution:
    def maxMagicalValue(self, arr):
        arr.sort(reverse=True)   # Sort descending
        max_val = float('-inf')
        prefix_sum = 0

        for i in range(len(arr)):
            prefix_sum += arr[i]
            curr_val = (i + 1) * prefix_sum
            max_val = max(max_val, curr_val)

        return max_val
    

