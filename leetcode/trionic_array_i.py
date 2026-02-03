from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # Check if array length is less than 3
        if n < 3:
            return False
        
        # Initialize variables to store p and q
        p, q = None, None
        
        # First pass to find p
        for i in range(1, n - 1):
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                p = i
                break
        
        # If no p is found, return False
        if p is None:
            return False
        
        # Second pass to find q
        for i in range(p + 1, n - 1):
            if nums[i - 1] > nums[i] and nums[i] < nums[i + 1]:
                q = i
                break
        
        # If no q is found, return False
        if q is None:
            return False
        
        # Validate the trionic condition
        is_increasing1 = all(nums[j] < nums[j + 1] for j in range(p))
        is_decreasing = all(nums[j] > nums[j + 1] for j in range(p, q))
        is_increasing2 = all(nums[j] < nums[j + 1] for j in range(q, n - 1))
        
        return is_increasing1 and is_decreasing and is_increasing2