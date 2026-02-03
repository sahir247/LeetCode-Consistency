from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # Check if the array length is less than 3
        if n < 3:
            return False
        
        # Initialize variables to track p and q
        p, q = None, None
        
        # First pass to find p and q
        increasing = True
        for i in range(1, n):
            if increasing:
                if nums[i] <= nums[i-1]:
                    if nums[i] == nums[i-1]:
                        return False
                    p = i - 1
                    increasing = False
            else:
                if nums[i] >= nums[i-1]:
                    if nums[i] == nums[i-1]:
                        return False
                    if p is not None:
                        q = i - 1
                        break
        
        # If p or q is not found, return False
        if p is None or q is None:
            return False
        
        # Check the third condition: nums[q...n-1] is strictly increasing
        for i in range(q + 1, n):
            if nums[i] <= nums[i-1]:
                return False
        
        # Check if 0 < p < q < n-1
        if not (0 < p < q < n - 1):
            return False
        
        return True