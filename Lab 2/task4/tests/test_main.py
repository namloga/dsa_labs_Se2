import unittest
import tracemalloc
import time
from task4.src.main import insert, find_k, Node


class TestTask4(unittest.TestCase):

    def test_bst_basic(self):
        input_data = [
            "+ 5",
            "+ 2",
            "+ 8",
            "+ 10",
            "+ 1",
            "? 1",
            "? 3",
            "? 5",
            "? 7",
            "? 0",
            "? 6"
        ]
        expected_output = ["1", "5", "10", "none", "none", "none"]

        start_time = time.time()
        tracemalloc.start()

        root = None
        result = []
        for line in input_data:
            if not line:
                continue
            if line.startswith('+'):
                x = int(line.split()[1])
                root = insert(root, x)
            elif line.startswith('?'):
                k = int(line.split()[1])
                value = find_k(root, k)
                result.append(str(value) if value is not None else "none")

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_output)
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10 ** 6, 256)

    def test_bst_min(self):
        input_data = ["+ 1", "? 1", "? 2"]
        expected_output = ["1", "none"]

        start_time = time.time()
        tracemalloc.start()

        root = None
        result = []
        for line in input_data:
            if not line:
                continue
            if line.startswith('+'):
                x = int(line.split()[1])
                root = insert(root, x)
            elif line.startswith('?'):
                k = int(line.split()[1])
                value = find_k(root, k)
                result.append(str(value) if value is not None else "none")

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_output)
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10 ** 6, 256)

    def test_bst_duplicate(self):
        input_data = ["+ 5", "+ 5", "+ 5", "? 1"]
        expected_output = ["5"]

        start_time = time.time()
        tracemalloc.start()

        root = None
        result = []
        for line in input_data:
            if not line:
                continue
            if line.startswith('+'):
                x = int(line.split()[1])
                root = insert(root, x)
            elif line.startswith('?'):
                k = int(line.split()[1])
                value = find_k(root, k)
                result.append(str(value) if value is not None else "none")

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_output)
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10 ** 6, 256)

    def test_bst_large_duplicates(self):
        input_data = [
            "+ 10", "+ 15", "+ 10", "+ 20", "+ 25",
            "+ 10", "+ 30", "+ 35", "+ 40", "+ 10",
            "+ 15", "+ 20", "+ 25", "+ 30", "+ 10",
            "+ 5", "+ 5", "+ 5", "+ 40", "+ 35"
        ]

        unique_numbers = sorted({5, 10, 15, 20, 25, 30, 35, 40})

        k_values = [1, 3, 5, 7, 10]

        expected_output = [str(unique_numbers[k - 1]) if k <= len(unique_numbers) else "none" for k in k_values]

        start_time = time.time()
        tracemalloc.start()

        root = None
        result = []
        for line in input_data:
            if line.startswith('+'):
                x = int(line.split()[1])
                root = insert(root, x)

        for k in k_values:
            value = find_k(root, k)
            result.append(str(value) if value is not None else "none")

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_output)
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10 ** 6, 256)


if __name__ == '__main__':
    unittest.main()
