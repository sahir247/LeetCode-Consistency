from typing import List

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = float('-inf')
        for l in range(n - 3):
            sum_first_segment = 0
            max_sum_first_segment = float('-inf')
            for p in range(l + 1, n - 2):
                sum_first_segment += nums[p]
                max_sum_first_segment = max(max_sum_first_segment, sum_first_segment)
                sum_second_segment = 0
                max_sum_second_segment = float('-inf')
                for q in range(p + 1, n - 1):
                    sum_second_segment += nums[q]
                    max_sum_second_segment = max(max_sum_second_segment, sum_second_segment)
                    sum_third_segment = 0
                    for r in range(q + 1, n):
                        sum_third_segment += nums[r]
                        current_sum = max(0, max_sum_first_segment) + max_sum_second_segment + max(0, sum_third_segment)
                        max_sum = max(max_sum, current_sum)
        return max_sum