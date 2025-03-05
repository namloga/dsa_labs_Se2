import unittest
import tracemalloc
import time
from task17.src.main import Solve  # Đảm bảo `Solve` là hàm chính của bạn

class TestTask17(unittest.TestCase):

    def test_case_1(self):
        N = 1
        expected_result = 8

        start_time = time.time()
        tracemalloc.start()
        result = Solve(N)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_result)
        self.assertLess(execution_time, 1)
        self.assertLess(peak / 10 ** 6, 256)

    def test_case_2(self):
        N = 2
        expected_result = 16

        start_time = time.time()
        tracemalloc.start()
        result = Solve(N)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_result)
        self.assertLess(execution_time, 1)
        self.assertLess(peak / 10 ** 6, 256)

    def test_case_3(self):
        N = 3
        expected_result = 36

        start_time = time.time()
        tracemalloc.start()
        result = Solve(N)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_result)
        self.assertLess(execution_time, 1)
        self.assertLess(peak / 10 ** 6, 256)

    def test_case_4(self):
        N = 10
        expected_result = 11728

        start_time = time.time()
        tracemalloc.start()
        result = Solve(N)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_result)
        self.assertLess(execution_time, 1)
        self.assertLess(peak / 10 ** 6, 256)

    def test_case_5(self):
        N = 1000

        start_time = time.time()
        tracemalloc.start()
        result = Solve(N)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertLess(execution_time, 1)
        self.assertLess(peak / 10 ** 6, 256)

if __name__ == '__main__':
    unittest.main()
