from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        p = 0
        while p < n - 1 and nums[p] < nums[p + 1]:
            p += 1
        if p == n - 1:
            return False
        q = p + 1
        while q < n - 1 and nums[q] > nums[q + 1]:
            q += 1
        if q == p + 1:
            return False
        while q < n - 1 and nums[q] < nums[q + 1]:
            q += 1
        return q == n - 1