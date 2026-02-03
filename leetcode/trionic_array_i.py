from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 5:
            return False
        
        # Find peak (p)
        p = -1
        for i in range(1, n - 1):
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                p = i
                break
        if p == -1:
            return False
        
        # Find trough (q)
        q = -1
        for i in range(p + 1, n - 1):
            if nums[i - 1] > nums[i] and nums[i] < nums[i + 1]:
                q = i
                break
        if q == -1:
            return False
        
        # Check if subarrays are strictly increasing/decreasing
        if not all(nums[j] < nums[j + 1] for j in range(p)):
            return False
        if not all(nums[j] > nums[j + 1] for j in range(p, q)):
            return False
        if not all(nums[j] < nums[j + 1] for j in range(q, n - 1)):
            return False
        
        return True