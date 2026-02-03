from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False
        state = 'increasing'
        peak = False
        valley = False
        for i in range(1, n):
            if state == 'increasing':
                if nums[i] <= nums[i-1]:
                    if nums[i] == nums[i-1]:
                        return False
                    state = 'decreasing'
                    peak = True
            elif state == 'decreasing':
                if nums[i] >= nums[i-1]:
                    if nums[i] == nums[i-1]:
                        return False
                    state = 'increasing'
                    valley = True
                    if not peak:
                        return False
        return valley and peak