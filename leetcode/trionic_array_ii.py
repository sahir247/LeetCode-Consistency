from typing import List

class Solution:
    def solution(self, nums: List[int]) -> int:
        n = len(nums)
        left_min_sum = [0]*n
        right_min_sum = [0]*n
        min_sum = 0
        for i in range(n):
            min_sum = min(min_sum, 0) + nums[i]
            left_min_sum[i] = min_sum
        min_sum = 0
        for i in range(n-1, -1, -1):
            min_sum = min(min_sum, 0) + nums[i]
            right_min_sum[i] = min_sum
        max_sum = float('-inf')
        for i in range(1, n-1):
            max_sum = max(max_sum, left_min_sum[i-1] + nums[i] + right_min_sum[i+1])
        return max_sum