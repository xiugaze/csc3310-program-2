import pytest
import selection_sort


def test_sort():
    # Test with positive numbers
    input = [4, 3, 2, 1]
    selection_sort.sort(input)
    assert input == [1, 2, 3, 4]

    # Test with already sorted list
    input = [1, 2, 3, 4]
    selection_sort.sort(input)
    assert input == [1, 2, 3, 4]

    # Test with negative numbers
    input = [-4, -3, -2, -1]
    selection_sort.sort(input)
    assert input == [-4, -3, -2, -1]

    input = [-1, -2, -3, -4]
    selection_sort.sort(input)
    assert input == [-4, -3, -2, -1]

    # Test with mixed numbers
    input = [-4, 3, -2, 1]
    selection_sort.sort(input)
    assert input == [-4, -2, 1, 3]

    input = [4, -3, 2, -1]
    selection_sort.sort(input)
    assert input == [-3, -1, 2, 4]

    # Test with empty list
    input = []
    selection_sort.sort(input)
    assert input == []

    # Test with single element
    input = [1]
    selection_sort.sort(input)
    assert input == [1]

    # Test with two elements
    input = [2, 1]
    selection_sort.sort(input)
    assert input == [1, 2]

    # Test with large list
    input = list(range(1000, 0, -1))
    selection_sort.sort(input)
    assert input == list(range(1, 1001))