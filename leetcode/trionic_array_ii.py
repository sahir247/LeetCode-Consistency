from typing import List

class Solution:
    def solution(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        def get_sum(l, r):
            return prefix_sum[r + 1] - prefix_sum[l]
        
        min_sum = [float('inf')] * n
        min_sum[0] = nums[0]
        for i in range(1, n):
            min_sum[i] = min(min_sum[i - 1], nums[i])
        
        max_sum = float('-inf')
        for q in range(2, n - 1):
            max_left_sum = float('-inf')
            for p in range(1, q):
                left_sum = get_sum(0, p - 1) - min_sum[p - 1]
                max_left_sum = max(max_left_sum, left_sum)
            max_right_sum = float('-inf')
            for r in range(q + 1, n):
                right_sum = get_sum(q + 1, r) - min_sum[r]
                max_right_sum = max(max_right_sum, right_sum)
            max_sum = max(max_sum, max_left_sum + nums[q] + max_right_sum)
        return max_sum