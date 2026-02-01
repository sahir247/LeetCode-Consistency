import pytest
from algorithms.implement_quicksort_in_python_ import quicksort

def test_empty():
    assert quicksort([]) == []

def test_single():
    assert quicksort([5]) == [5]

def test_unsorted():
    assert quicksort([3,1,2]) == [1,2,3]