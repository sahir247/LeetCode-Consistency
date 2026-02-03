from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        increasing = nums[1] > nums[0]
        p = q = -1
        for i in range(1, n):
            if nums[i] == nums[i-1]:
                return False
            new_increasing = nums[i] > nums[i-1]
            if increasing != new_increasing:
                if increasing:  # trend changed from increasing to decreasing
                    p = i - 1
                    if p == 0:  # p cannot be the first index
                        return False
                else:  # trend changed from decreasing to increasing
                    q = i - 1
                    if q <= p:  # q must be after p
                        return False
                increasing = new_increasing
        
        return p != -1 and q != -1 and q < n - 1