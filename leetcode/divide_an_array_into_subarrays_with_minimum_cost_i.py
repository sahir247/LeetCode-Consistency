class Solution:
    def minimumCost(self, nums):
        if len(nums) < 3:
            return sum(nums)
        cost = 0
        for i in range(len(nums)-2):
            cost += nums[i]
            nums[i+2] += nums[i+1]
        cost += nums[-1]
        return cost