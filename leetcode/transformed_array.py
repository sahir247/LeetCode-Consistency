from typing import List

class Solution:
    def solution(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        for i in range(n):
            new_index = ((i + nums[i]) % n + n) % n
            result[new_index] = nums[i] if nums[i] != 0 else 0
        return result