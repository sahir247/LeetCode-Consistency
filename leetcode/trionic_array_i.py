from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        trend_changes = 0
        current_trend = None
        for i in range(1, len(nums)):
            new_trend = None
            if nums[i] > nums[i-1]:
                new_trend = 'increasing'
            elif nums[i] < nums[i-1]:
                new_trend = 'decreasing'
            else:
                return False
            if current_trend is not None and new_trend != current_trend:
                trend_changes += 1
                if trend_changes > 2:
                    return False
            current_trend = new_trend
        return trend_changes == 2 and current_trend == 'increasing'