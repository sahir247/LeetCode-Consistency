from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # Check all possible p and q
        for p in range(1, n-2):
            for q in range(p+1, n-1):
                # Check if nums[0...p] is strictly increasing
                increasing1 = all(nums[i] < nums[i+1] for i in range(p))
                # Check if nums[p...q] is strictly decreasing
                decreasing = all(nums[i] > nums[i+1] for i in range(p, q))
                # Check if nums[q...n-1] is strictly increasing
                increasing2 = all(nums[i] < nums[i+1] for i in range(q, n-1))
                
                # If all conditions are met, return True
                if increasing1 and decreasing and increasing2:
                    return True
        
        # If no suitable p and q are found, return False
        return False