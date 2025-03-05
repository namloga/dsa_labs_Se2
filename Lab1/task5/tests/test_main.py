import unittest
import tracemalloc
import time
from task5.src.main import Solve


class TestTask5(unittest.TestCase):

    def test_prizes_basic(self):

        n = 6
        expected_k = 3
        expected_output = [1, 2, 3]

        start_time = time.time()
        tracemalloc.start()
        k, result = Solve(n)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(k, expected_k)
        self.assertEqual(result, expected_output)
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10 ** 6, 100)

    def test_prizes_large_n(self):

        n = 15
        expected_k = 5
        expected_output = [1, 2, 3, 4, 5]

        start_time = time.time()
        tracemalloc.start()
        k, result = Solve(n)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(k, expected_k)
        self.assertEqual(result, expected_output)
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10 ** 6, 100)

    def test_prizes_not_exact_series(self):

        n = 8
        expected_k = 3
        expected_output = [1, 2, 5]

        start_time = time.time()
        tracemalloc.start()
        k, result = Solve(n)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(k, expected_k)
        self.assertEqual(result, expected_output)
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10 ** 6, 100)

    def test_prizes_min_n(self):

        n = 1
        expected_k = 1
        expected_output = [1]

        start_time = time.time()
        tracemalloc.start()
        k, result = Solve(n)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(k, expected_k)
        self.assertEqual(result, expected_output)
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10 ** 6, 100)


if __name__ == '__main__':
    unittest.main()
