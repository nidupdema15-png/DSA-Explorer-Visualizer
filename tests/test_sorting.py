import unittest
from dsa_logic import bubble_sort_steps, selection_sort_steps


class TestSorting(unittest.TestCase):

    def test_bubble_sort(self):
        array = [5, 3, 8, 1, 2]
        steps = bubble_sort_steps(array)
        final_array = steps[-1][0]
        self.assertEqual(final_array, [1, 2, 3, 5, 8])

    def test_selection_sort(self):
        array = [9, 4, 7, 1, 6]
        steps = selection_sort_steps(array)
        final_array = steps[-1][0]
        self.assertEqual(final_array, [1, 4, 6, 7, 9])


if __name__ == "__main__":
    unittest.main()
