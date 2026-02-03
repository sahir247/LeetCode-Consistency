import pytest
from leetcode.divide_an_array_into_subarrays_with_minimum_cost_i import Solution

def test_empty():
    assert Solution().minimumCost([]) == float('inf')

def test_single():
    assert Solution().minimumCost([5]) == 5

def test_unsorted():
    assert Solution().minimumCost([3,1,2]) == 6
