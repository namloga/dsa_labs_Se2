import unittest
import tracemalloc
import time
from task14.src.main import Solve  # Đảm bảo `Solve` là hàm chính của bạn


class TestTask14(unittest.TestCase):

    def test_case_1(self):
        expression = "5-8+7*4-8+9"
        expected_result = 200

        start_time = time.time()
        tracemalloc.start()
        result = Solve(expression)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_result)
        self.assertLess(execution_time, 5)
        self.assertLess(peak / 10 ** 6, 10)

    def test_case_2(self):
        expression = "1+5"
        expected_result = 6

        start_time = time.time()
        tracemalloc.start()
        result = Solve(expression)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_result)
        self.assertLess(execution_time, 5)
        self.assertLess(peak / 10 ** 6, 10)

    def test_case_3(self):
        expression = "2*3*4"
        expected_result = 24

        start_time = time.time()
        tracemalloc.start()
        result = Solve(expression)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_result)
        self.assertLess(execution_time, 5)
        self.assertLess(peak / 10 ** 6, 10)

    def test_case_4(self):
        expression = "9-5-3"
        expected_result = 7

        start_time = time.time()
        tracemalloc.start()
        result = Solve(expression)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_result)
        self.assertLess(execution_time, 5)
        self.assertLess(peak / 10 ** 6, 10)

    def test_case_5(self):
        expression = "2*5+3-6*4"
        expected_result = 40

        start_time = time.time()
        tracemalloc.start()
        result = Solve(expression)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_result)
        self.assertLess(execution_time, 5)
        self.assertLess(peak / 10 ** 6, 10)

    def test_case_6(self):
        expression = "7"
        expected_result = 7

        start_time = time.time()
        tracemalloc.start()
        result = Solve(expression)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_result)
        self.assertLess(execution_time, 5)
        self.assertLess(peak / 10 ** 6, 10)


if __name__ == '__main__':
    unittest.main()
