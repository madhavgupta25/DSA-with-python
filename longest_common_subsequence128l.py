from __future__ import annotationsit
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start_map = {}
        for x in nums:
            if x-1 in start_map:
                start_map[x] = False
            else:
                start_map[x] = True
            
            if x + 1 in start_map:
                start_map[x+1] = False
        max_so_far = 0

        for key , val in start_map.items():
            if val == True:
                cnt = 0
                while key in start_map:
                    cnt+=1
                    key+=1
                max_so_far = max(max_so_far , cnt)
                
        return max_so_far
    
    
s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))


        