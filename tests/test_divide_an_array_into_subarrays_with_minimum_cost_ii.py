import pytest
from leetcode.divide_an_array_into_subarrays_with_minimum_cost_ii import Solution

def test_empty():
    sol = Solution()
    assert sol.minimumCost([], 3, 2) == 0

def test_single():
    sol = Solution()
    assert sol.minimumCost([5], 1, 1) == 5

def test_normal_case():
    sol = Solution()
    assert sol.minimumCost([1, 4, 1, 5], 2, 2) == 5