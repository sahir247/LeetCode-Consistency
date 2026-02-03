from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        increasing = decreasing = False
        p = q = -1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                if decreasing:
                    q = i - 1
                    break
                increasing = True
            elif nums[i] < nums[i - 1]:
                if not increasing:
                    return False
                decreasing = True
            else:
                return False
        
        if not decreasing:
            return False
        
        for j in range(q + 1, n):
            if nums[j] <= nums[j - 1]:
                return False
        
        p = next((i for i in range(1, n) if nums[i] < nums[i - 1]), -1)
        if p == -1 or q == -1 or p >= q:
            return False
        
        return 0 < p < q < n - 1