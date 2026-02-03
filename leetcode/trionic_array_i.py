from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 5:
            return False
        trend = 'increasing'
        p, q = None, None
        for i in range(1, n):
            if trend == 'increasing':
                if nums[i] <= nums[i-1]:
                    if p is None:
                        p = i - 1
                        trend = 'decreasing'
                    else:
                        return False
            elif trend == 'decreasing':
                if nums[i] >= nums[i-1]:
                    q = i - 1
                    trend = 'increasing'
            if i == n - 1 and q is None:
                return False
        return p is not None and q is not None and 0 < p < q < n - 1