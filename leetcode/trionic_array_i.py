from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        p, q = -1, -1
        for i in range(1, n - 1):
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                p = i
                break
        if p == -1:
            return False
        for i in range(p + 1, n - 1):
            if nums[i - 1] > nums[i] and nums[i] < nums[i + 1]:
                q = i
                break
        if q == -1:
            return False
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