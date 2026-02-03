from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        trend = None
        p = q = None
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                if trend == 'decreasing':
                    q = i-1
                    trend = 'increasing'
                elif trend is None:
                    trend = 'increasing'
                elif trend == 'increasing':
                    pass
                else:
                    return False
            elif nums[i] < nums[i-1]:
                if trend == 'increasing':
                    p = i-1
                    trend = 'decreasing'
                elif trend is None:
                    return False
                elif trend == 'decreasing':
                    pass
                else:
                    return False
            else:
                return False
        if p is not None and q is not None and p < q:
            return True
        return False