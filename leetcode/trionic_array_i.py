from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # Initialize variables to store the state
        state = 0  # 0: increasing, 1: decreasing, 2: increasing again
        
        # Initialize p and q
        p = q = -1
        
        for i in range(n - 1):
            if state == 0:
                if nums[i] >= nums[i + 1]:
                    if i == 0:  # If the first two elements are not increasing, return False
                        return False
                    p = i
                    state = 1
            elif state == 1:
                if nums[i] <= nums[i + 1]:
                    q = i
                    state = 2
            elif state == 2:
                if nums[i] >= nums[i + 1]:
                    return False  # If it's not increasing after q, return False
        
        # Check if we have found valid p and q
        if p == -1 or q == -1 or q == n - 1:
            return False
        
        # Check the conditions again to ensure correctness
        for i in range(p):
            if nums[i] >= nums[i + 1]:
                return False
        for i in range(p, q):
            if nums[i] <= nums[i + 1]:
                return False
        for i in range(q, n - 1):
            if nums[i] >= nums[i + 1]:
                return False
        
        return True