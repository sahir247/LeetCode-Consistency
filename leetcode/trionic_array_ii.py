from typing import List

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        def sum_subarray(l, r):
            return prefix_sum[r + 1] - prefix_sum[l]
        
        max_sum = float('-inf')
        for p in range(1, n - 2):
            for q in range(p + 1, n - 1):
                min_sum_first = float('inf')
                for l in range(p):
                    min_sum_first = min(min_sum_first, sum_subarray(l, p - 1))
                max_sum_first = max(0, -min_sum_first)
                
                sum_second = sum_subarray(p, q)
                
                min_sum_third = float('inf')
                for r in range(q + 1, n):
                    min_sum_third = min(min_sum_third, sum_subarray(q + 1, r))
                max_sum_third = max(0, -min_sum_third)
                
                max_sum = max(max_sum, max_sum_first + sum_second + max_sum_third)
        return max_sum