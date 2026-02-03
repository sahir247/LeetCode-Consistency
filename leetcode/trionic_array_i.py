from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False
        p, q = -1, -1
        # Find peak (p)
        for i in range(1, n - 1):
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                p = i
                break
        if p == -1:
            return False
        # Find trough (q)
        for i in range(p + 1, n - 1):
            if nums[i - 1] > nums[i] and nums[i] < nums[i + 1]:
                q = i
                break
        if q == -1:
            return False
        # Check if subarrays satisfy trionic conditions
        for i in range(1, p):
            if nums[i - 1] >= nums[i]:
                return False
        for i in range(p + 1, q):
            if nums[i - 1] <= nums[i]:
                return False
        for i in range(q + 1, n):
            if nums[i - 1] >= nums[i]:
                return False
        return True