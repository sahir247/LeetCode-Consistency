from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 6:
            return False
        state = 'increasing'
        p = q = None
        for i in range(1, n):
            if state == 'increasing':
                if nums[i] <= nums[i-1]:
                    if i == 1:
                        return False
                    state = 'decreasing'
                    p = i - 1
            elif state == 'decreasing':
                if nums[i] >= nums[i-1]:
                    state = 'increasing'
                    q = i - 1
            if state == 'increasing' and q is not None:
                if nums[i] <= nums[i-1]:
                    return False
        return q is not None and p < q