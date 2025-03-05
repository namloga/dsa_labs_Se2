import unittest
import tracemalloc
import time
from task1.src.main import Solve


class TestTask1(unittest.TestCase):

    def test_knapsack_basic(self):
        arr = [
            [60, 20],
            [100, 50],
            [120, 30]
        ]
        n = 3
        w = 50
        expected_output = '180.0000'

        start_time = time.time()
        tracemalloc.start()
        result = Solve(3, 50, arr)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_output)
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10 ** 6, 100)

    def test_knapsack_single_item(self):
        arr = [
            [500, 30]
        ]
        n = 1
        w = 10
        expected_output = '166.6667'

        start_time = time.time()
        tracemalloc.start()
        result = Solve(n, w, arr)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_output)
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10 ** 6, 100)

    def test_knapsack_large_capacity(self):
        arr = [
            [60, 10],
            [100, 20],
            [120, 15]
        ]
        n = 3
        w = 30
        expected_output = '205.0000'

        start_time = time.time()
        tracemalloc.start()
        result = Solve(n, w, arr)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_output)
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10 ** 6, 100)

    def test_knapsack_no_capacity(self):
        arr = [
            [100, 10],
            [200, 20]
        ]
        n = 2
        w = 0
        expected_output = '0.0000'

        start_time = time.time()
        tracemalloc.start()
        result = Solve(n, w, arr)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_output)
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10 ** 6, 100)


if __name__ == '__main__':
    unittest.main()
