"""
Property-based tests for sorting algorithms using Hypothesis.
"""

from hypothesis import given, strategies as st
from .bubble_sort import bubble_sort
from .merge_sort import merge_sort
from .quick_sort import quick_sort


@given(st.lists(st.integers()))
def test_bubble_sort_matches_sorted(xs):
    assert bubble_sort(xs) == sorted(xs)


@given(st.lists(st.integers()))
def test_merge_sort_matches_sorted(xs):
    assert merge_sort(xs) == sorted(xs)


@given(st.lists(st.integers()))
def test_quick_sort_matches_sorted(xs):
    assert quick_sort(xs) == sorted(xs)
