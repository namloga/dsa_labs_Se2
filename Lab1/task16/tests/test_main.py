import unittest
import tracemalloc
import time
from task16.src.main import Solve

class TestTask16(unittest.TestCase):

    def test_case_1(self):

        n = 5
        distances = [
            [0, 183, 163, 173, 181],
            [183, 0, 165, 172, 171],
            [163, 165, 0, 189, 302],
            [173, 172, 189, 0, 167],
            [181, 171, 302, 167, 0]
        ]
        expected_cost = 666
        expected_path = [4, 5, 2, 3, 1]

        start_time = time.time()
        tracemalloc.start()
        result_cost, result_path = Solve(n, distances)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result_cost, expected_cost)
        self.assertEqual(result_path, expected_path)
        self.assertLess(execution_time, 1)
        self.assertLess(peak / 10 ** 6, 256)

    def test_case_2(self):
        n = 4
        distances = [
            [0, 10, 15, 20],
            [10, 0, 35, 25],
            [15, 35, 0, 30],
            [20, 25, 30, 0]
        ]
        expected_cost = 50
        expected_path =  [4, 2, 1, 3]

        start_time = time.time()
        tracemalloc.start()
        result_cost, result_path = Solve(n, distances)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result_cost, expected_cost)
        self.assertEqual(result_path, expected_path)
        self.assertLess(execution_time, 1)
        self.assertLess(peak / 10 ** 6, 256)

    def test_case_3(self):
        n = 3
        distances = [
            [0, 29, 20],
            [29, 0, 15],
            [20, 15, 0]
        ]
        expected_cost = 35
        expected_path = [2, 3, 1]

        start_time = time.time()
        tracemalloc.start()
        result_cost, result_path = Solve(n, distances)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result_cost, expected_cost)
        self.assertEqual(result_path, expected_path)
        self.assertLess(execution_time, 1)
        self.assertLess(peak / 10 ** 6, 256)

    def test_case_4(self):
        n = 5
        distances = [
            [0, 100, 200, 300, 400],
            [100, 0, 150, 250, 350],
            [200, 150, 0, 180, 280],
            [300, 250, 180, 0, 170],
            [400, 350, 280, 170, 0]
        ]
        expected_cost = 600
        expected_path = [5, 4, 3, 2, 1]

        start_time = time.time()
        tracemalloc.start()
        result_cost, result_path = Solve(n, distances)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result_cost, expected_cost)
        self.assertEqual(result_path, expected_path)
        self.assertLess(execution_time, 1)
        self.assertLess(peak / 10 ** 6, 256)


if __name__ == '__main__':
    unittest.main()
