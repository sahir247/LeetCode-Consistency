class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(k)]
        for j in range(n):
            dp[0][j] = sum(nums[:j+1])
        for i in range(1, k):
            for j in range(i, n):
                min_cost = float('inf')
                for m in range(max(i-1, j-dist), j):
                    min_cost = min(min_cost, dp[i-1][m] + sum(nums[m+1:j+1]))
                dp[i][j] = min_cost
        return dp[-1][-1