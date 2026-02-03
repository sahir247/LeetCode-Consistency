class Solution:
    def minimumCost(self, nums):
        n = len(nums)
        if n < 3:
            return sum(nums)

        total_sum = sum(nums)
        target_sum = total_sum // 3

        sum1, sum2, sum3 = 0, 0, 0
        min_cost = float('inf')

        for num in nums:
            if sum1 <= target_sum and (sum2 + num) / 2 <= target_sum:
                sum1 += num
                min_cost = min(min_cost, num)
            elif sum2 <= target_sum and (sum3 + num) / 2 <= target_sum:
                sum2 += num
                min_cost = min(min_cost, num)
            else:
                sum3 += num
                min_cost = min(min_cost, num)

        return min_cost