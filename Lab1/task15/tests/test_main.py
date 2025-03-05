import unittest
import tracemalloc
import time
from task15.src.main import Solve


class TestTask15(unittest.TestCase):

    def test_case_1(self):
        s = "([)]"
        expected_result = "[]"

        start_time = time.time()
        tracemalloc.start()
        result = Solve(s)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_result)
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10 ** 6, 10)

    def test_case_2(self):
        s = "{[()]}"
        expected_result = "{[()]}"

        start_time = time.time()
        tracemalloc.start()
        result = Solve(s)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_result)
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10 ** 6, 10)

    def test_case_3(self):
        s = ")))"
        expected_result = ""

        start_time = time.time()
        tracemalloc.start()
        result = Solve(s)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_result)
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10 ** 6, 10)

    def test_case_4(self):
        s = "{(})[()"
        expected_result = "()()"

        start_time = time.time()
        tracemalloc.start()
        result = Solve(s)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_result)
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10 ** 6, 10)

    def test_case_5(self):
        s = ""
        expected_result = ""

        start_time = time.time()
        tracemalloc.start()
        result = Solve(s)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_result)
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10 ** 6, 10)

    def test_case_6(self):
        s = "(((([[[[{{{{}}}}]]]]))))"
        expected_result = "(((([[[[{{{{}}}}]]]]))))"

        start_time = time.time()
        tracemalloc.start()
        result = Solve(s)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_result)
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10 ** 6, 10)


if __name__ == '__main__':
    unittest.main()
