from typing import List

class Solution:
    def solution(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        for i in range(n):
            result[((i + nums[i]) % n + n) % n] = nums[i] if nums[i] == 0 else nums[((i + nums[i]) % n + n) % n]
        return result