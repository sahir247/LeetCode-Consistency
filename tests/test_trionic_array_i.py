import pytest
from leetcode.trionic_array_i import Solution

def test_example_1():
    sol = Solution()
    assert sol.isTrionic([1, 3, 5, 4, 2, 6]) == True

def test_example_2():
    sol = Solution()
    assert sol.isTrionic([2, 1, 3]) == False