from typing import List

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = float('-inf')
        for l in range(n-3):
            sum_first_segment = sum(nums[l:l+1])
            min_sum_second_segment = float('inf')
            max_sum_second_segment = float('-inf')
            sum_second_segment = 0
            for p in range(l+1, n-2):
                sum_second_segment += nums[p]
                min_sum_second_segment = min(min_sum_second_segment, sum_second_segment)
                max_sum_second_segment = max(max_sum_second_segment, sum_second_segment)
                for q in range(p+1, n-1):
                    sum_third_segment = sum(nums[q:q+1])
                    for r in range(q+1, n):
                        sum_third_segment += nums[r]
                        current_sum = max(0, sum_first_segment) + max_sum_second_segment + max(0, sum_third_segment)
                        max_sum = max(max_sum, current_sum)
                        current_sum = max(0, sum_first_segment) + sum_second_segment + max(0, sum_third_segment)
                        max_sum = max(max_sum, current_sum)
        return max_sum