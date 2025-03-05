import unittest
import tracemalloc
import time
from task20.src.main import Solve  # Đảm bảo `Solve` là hàm chính của bạn


class TestTask20(unittest.TestCase):

    def test_case_1(self):
        n = 5
        k = 1
        s = "ababa"
        expected_result = 13

        start_time = time.time()
        tracemalloc.start()
        result = Solve(n, k, s)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_result)
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10 ** 6, 256)

    def test_case_2(self):
        n = 6
        k = 2
        s = "aaaaaa"
        expected_result = 21

        start_time = time.time()
        tracemalloc.start()
        result = Solve(n, k, s)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_result)
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10 ** 6, 256)

    def test_case_3(self):
        n = 4
        k = 0
        s = "abca"
        expected_result = 4

        start_time = time.time()
        tracemalloc.start()
        result = Solve(n, k, s)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_result)
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10 ** 6, 256)

    def test_case_4(self):
        n = 10
        k = 2
        s = "abacabadab"
        expected_result = 46

        start_time = time.time()
        tracemalloc.start()
        result = Solve(n, k, s)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_result)
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10 ** 6, 256)

    def test_case_5(self):
        n = 6
        k = 6
        s = "abcdef"
        expected_result = 21

        start_time = time.time()
        tracemalloc.start()
        result = Solve(n, k, s)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_result)
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10 ** 6, 256)


if __name__ == '__main__':
    unittest.main()
