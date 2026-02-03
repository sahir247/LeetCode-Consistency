from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        
        for p in range(1, n-1):
            # Check if nums[0...p] is strictly increasing
            if all(nums[i] < nums[i+1] for i in range(p)):
                for q in range(p+1, n-1):
                    # Check if nums[p...q] is strictly decreasing
                    if all(nums[i] > nums[i+1] for i in range(p, q)):
                        # Check if nums[q...n-1] is strictly increasing
                        if all(nums[i] < nums[i+1] for i in range(q, n-1)):
                            return True
        return False