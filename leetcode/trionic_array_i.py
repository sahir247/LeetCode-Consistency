from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        trend_changes = 0
        current_trend = None
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                new_trend = 'increasing'
            elif nums[i] < nums[i-1]:
                new_trend = 'decreasing'
            else:
                new_trend = current_trend
            if new_trend != current_trend:
                trend_changes += 1
                if trend_changes > 3:
                    return False
            current_trend = new_trend
        return trend_changes == 3 and current_trend == 'increasing'