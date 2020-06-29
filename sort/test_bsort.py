from unittest import TestCase
from sort import bsort


class TestBubbleSort(TestCase):
    def test_bubble_sort_small_num(self):
        nlist = list([2, 1])
        assert bsort.bubble_sort(nlist)["sorted_list"] == sorted(nlist)

    def test_bubble_sort_big_num(self):
        nlist = list([58, 14, 92, 27, 62, 19, 7, 66])
        assert bsort.bubble_sort(nlist)["sorted_list"] == sorted(nlist)

    def test_bubble_sort_small_string(self):
        nlist = list(["z", "a"])
        assert bsort.bubble_sort(nlist)["sorted_list"] == sorted(nlist)
