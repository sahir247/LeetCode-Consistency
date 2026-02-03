from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        # Find peak (p)
        p = 0
        while p < n - 1 and nums[p] <= nums[p + 1]:
            p += 1
        if p == 0 or p == n - 1:
            return False
        
        # Find trough (q)
        q = p
        while q < n - 1 and nums[q] >= nums[q + 1]:
            q += 1
        if q == p or q == n - 1:
            return False
        
        # Check if subarrays satisfy the required conditions
        return (all(nums[i] < nums[i + 1] for i in range(p)) and
                all(nums[i] > nums[i + 1] for i in range(p, q)) and
                all(nums[i] < nums[i + 1] for i in range(q, n - 1)))
    