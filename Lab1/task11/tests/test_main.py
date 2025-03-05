import unittest
import tracemalloc
import time
from task11.src.main import Solve


class TestTask11(unittest.TestCase):

    def test_knapsack_basic(self):
        W = 10
        weights = [1, 4, 8]
        expected_output = 9

        start_time = time.time()
        tracemalloc.start()
        result = Solve(W, weights)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_output)
        self.assertLess(execution_time, 5)
        self.assertLess(peak / 10 ** 6, 100)

    def test_knapsack_large_capacity(self):
        W = 20
        weights = [5, 7, 12, 18, 1]
        expected_output = 20

        start_time = time.time()
        tracemalloc.start()
        result = Solve(W, weights)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_output)
        self.assertLess(execution_time, 5)
        self.assertLess(peak / 10 ** 6, 100)

    def test_knapsack_exact_fit(self):
        W = 15
        weights = [3, 5, 7]
        expected_output = 15

        start_time = time.time()
        tracemalloc.start()
        result = Solve(W, weights)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_output)
        self.assertLess(execution_time, 5)
        self.assertLess(peak / 10 ** 6, 100)

    def test_knapsack_no_space(self):
        W = 3
        weights = [5, 7, 9]
        expected_output = 0

        start_time = time.time()
        tracemalloc.start()
        result = Solve(W, weights)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_output)
        self.assertLess(execution_time, 5)
        self.assertLess(peak / 10 ** 6, 100)


if __name__ == '__main__':
    unittest.main()
