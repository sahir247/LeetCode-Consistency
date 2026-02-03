from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        trend = 0  # 0: unknown, 1: increasing, -1: decreasing
        peak_trough_count = 0
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                if trend == -1:  # Switch from decreasing to increasing
                    peak_trough_count += 1
                    if peak_trough_count > 2:
                        return False
                trend = 1
            elif nums[i] < nums[i-1]:
                if trend == 1:  # Switch from increasing to decreasing
                    peak_trough_count += 1
                    if peak_trough_count > 2:
                        return False
                trend = -1
            else:
                return False  # Elements must be distinct
        
        return peak_trough_count == 2