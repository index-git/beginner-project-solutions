from unittest import TestCase
from Sort import sort


class TestBubbleSort(TestCase):
    def test_bubble_sort_small_num(self):
        nlist = list([2, 1])
        assert sort.bubble_sort(nlist)["sorted_list"] == sorted(nlist)

    def test_bubble_sort_big_num(self):
        nlist = list([58, 14, 92, 27, 62, 19, 7, 66])
        assert sort.bubble_sort(nlist)["sorted_list"] == sorted(nlist)

    def test_bubble_sort_small_string(self):
        nlist = list(["z", "a"])
        assert sort.bubble_sort(nlist)["sorted_list"] == sorted(nlist)
