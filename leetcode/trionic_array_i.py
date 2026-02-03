from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 5:
            return False
        trend = None
        p = q = None
        prev_num = nums[0]
        for i in range(1, n):
            curr_num = nums[i]
            if curr_num == prev_num:
                return False
            new_trend = 'increasing' if curr_num > prev_num else 'decreasing'
            if trend == 'increasing' and new_trend == 'decreasing':
                p = i - 1
            elif trend == 'decreasing' and new_trend == 'increasing':
                q = i - 1
            trend = new_trend
            prev_num = curr_num
        if p is None or q is None or p == 0 or q == n-1 or p >= q:
            return False
        return True