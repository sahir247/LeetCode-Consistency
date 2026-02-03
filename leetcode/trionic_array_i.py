from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        trend_changes = 0
        trend = None
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                new_trend = 'increasing'
            elif nums[i] < nums[i-1]:
                new_trend = 'decreasing'
            else:
                return False
            if trend == new_trend:
                continue
            if trend is not None:
                trend_changes += 1
                if trend_changes > 2:
                    return False
            trend = new_trend
        return trend_changes == 2 and trend == 'increasing'