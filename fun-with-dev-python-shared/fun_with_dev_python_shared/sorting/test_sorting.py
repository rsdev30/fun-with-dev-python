"""
Unit tests for sorting algorithms.

Tests cover:
- Empty lists
- Single elements
- Already sorted lists
- Reverse sorted lists
- Lists with duplicates
- Lists with negative numbers
- Random unsorted lists
"""

import pytest
from .bubble_sort import bubble_sort
from .merge_sort import merge_sort
from .quick_sort import quick_sort


class TestBubbleSort:
    """Tests for bubble sort implementation."""

    def test_empty_list(self):
        """Test sorting an empty list."""
        assert bubble_sort([]) == []

    def test_single_element(self):
        """Test sorting a single element."""
        assert bubble_sort([5]) == [5]

    def test_already_sorted(self):
        """Test sorting an already sorted list."""
        assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        """Test sorting a reverse sorted list."""
        assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_with_duplicates(self):
        """Test sorting a list with duplicate values."""
        assert bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]

    def test_with_negative_numbers(self):
        """Test sorting a list with negative numbers."""
        assert bubble_sort([5, -3, 0, 2, -1]) == [-3, -1, 0, 2, 5]

    def test_with_floats(self):
        """Test sorting a list of floats."""
        assert bubble_sort([3.5, 1.2, 4.8, 2.3]) == [1.2, 2.3, 3.5, 4.8]

    def test_large_list(self):
        """Test sorting a large list."""
        unsorted = list(range(100, 0, -1))
        expected = list(range(1, 101))
        assert bubble_sort(unsorted) == expected

    def test_two_elements(self):
        """Test sorting two elements."""
        assert bubble_sort([2, 1]) == [1, 2]

    def test_preserves_original(self):
        """Test that original list is not modified."""
        original = [3, 1, 4, 1, 5]
        original_copy = original.copy()
        bubble_sort(original)
        assert original == original_copy


class TestMergeSort:
    """Tests for merge sort implementation."""

    def test_empty_list(self):
        """Test sorting an empty list."""
        assert merge_sort([]) == []

    def test_single_element(self):
        """Test sorting a single element."""
        assert merge_sort([5]) == [5]

    def test_already_sorted(self):
        """Test sorting an already sorted list."""
        assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        """Test sorting a reverse sorted list."""
        assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_with_duplicates(self):
        """Test sorting a list with duplicate values."""
        assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]

    def test_with_negative_numbers(self):
        """Test sorting a list with negative numbers."""
        assert merge_sort([5, -3, 0, 2, -1]) == [-3, -1, 0, 2, 5]

    def test_with_floats(self):
        """Test sorting a list of floats."""
        assert merge_sort([3.5, 1.2, 4.8, 2.3]) == [1.2, 2.3, 3.5, 4.8]

    def test_large_list(self):
        """Test sorting a large list."""
        unsorted = list(range(100, 0, -1))
        expected = list(range(1, 101))
        assert merge_sort(unsorted) == expected

    def test_two_elements(self):
        """Test sorting two elements."""
        assert merge_sort([2, 1]) == [1, 2]

    def test_preserves_original(self):
        """Test that original list is not modified."""
        original = [3, 1, 4, 1, 5]
        original_copy = original.copy()
        merge_sort(original)
        assert original == original_copy


class TestQuickSort:
    """Tests for quick sort implementation."""

    def test_empty_list(self):
        """Test sorting an empty list."""
        assert quick_sort([]) == []

    def test_single_element(self):
        """Test sorting a single element."""
        assert quick_sort([5]) == [5]

    def test_already_sorted(self):
        """Test sorting an already sorted list."""
        assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        """Test sorting a reverse sorted list."""
        assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_with_duplicates(self):
        """Test sorting a list with duplicate values."""
        assert quick_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]

    def test_with_negative_numbers(self):
        """Test sorting a list with negative numbers."""
        assert quick_sort([5, -3, 0, 2, -1]) == [-3, -1, 0, 2, 5]

    def test_with_floats(self):
        """Test sorting a list of floats."""
        assert quick_sort([3.5, 1.2, 4.8, 2.3]) == [1.2, 2.3, 3.5, 4.8]

    def test_large_list(self):
        """Test sorting a large list."""
        unsorted = list(range(100, 0, -1))
        expected = list(range(1, 101))
        assert quick_sort(unsorted) == expected

    def test_two_elements(self):
        """Test sorting two elements."""
        assert quick_sort([2, 1]) == [1, 2]

    def test_preserves_original(self):
        """Test that original list is not modified."""
        original = [3, 1, 4, 1, 5]
        original_copy = original.copy()
        quick_sort(original)
        assert original == original_copy


class TestSortingConsistency:
    """Tests to ensure all sorting algorithms produce consistent results."""

    test_cases = [
        [],
        [1],
        [1, 2, 3],
        [3, 2, 1],
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
        [5, -3, 0, 2, -1, 10, -10],
        list(range(50, 0, -1)),
    ]

    @pytest.mark.parametrize("test_list", test_cases)
    def test_all_algorithms_consistent(self, test_list):
        """Test that all sorting algorithms produce the same result."""
        bubble_result = bubble_sort(test_list)
        merge_result = merge_sort(test_list)
        quick_result = quick_sort(test_list)

        assert bubble_result == merge_result == quick_result
        assert bubble_result == sorted(test_list)
