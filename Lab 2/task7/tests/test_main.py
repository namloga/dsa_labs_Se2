import unittest
import tracemalloc
import time
from task7.src.main import Node, is_bst

class TestTask7(unittest.TestCase):

    def test_bst_basic(self):
        input_data = [
            "3",
            "2 1 2",
            "1 -1 -1",
            "3 -1 -1"
        ]
        expected_output = "CORRECT"

        start_time = time.time()
        tracemalloc.start()

        n = int(input_data[0].strip())
        if n == 0:
            result = "CORRECT"
        else:
            tree = []
            for i in range(1, n + 1):
                k, l, r = map(int, input_data[i].split())
                tree.append(Node(k, l, r))

            result = "CORRECT" if is_bst(tree, 0, -2 ** 31, 2 ** 31 - 1) else "INCORRECT"

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_output)
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10 ** 6, 256)

    def test_bst_invalid(self):
        input_data = [
            "3",
            "2 1 2",
            "1 -1 -1",
            "0 -1 -1"
        ]
        expected_output = "INCORRECT"

        start_time = time.time()
        tracemalloc.start()

        n = int(input_data[0].strip())
        if n == 0:
            result = "CORRECT"
        else:
            tree = []
            for i in range(1, n + 1):
                k, l, r = map(int, input_data[i].split())
                tree.append(Node(k, l, r))

            result = "CORRECT" if is_bst(tree, 0, -2 ** 31, 2 ** 31 - 1) else "INCORRECT"

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_output)
        self.assertLess(execution_time, 10)
        self.assertLess(peak / 10 ** 6, 512)

    def test_bst_large_valid(self):
        input_data = [
            "7",
            "4 1 2",
            "2 3 4",
            "6 5 6",
            "1 -1 -1",
            "3 -1 -1",
            "5 -1 -1",
            "7 -1 -1"
        ]
        expected_output = "CORRECT"

        start_time = time.time()
        tracemalloc.start()

        n = int(input_data[0].strip())
        if n == 0:
            result = "CORRECT"
        else:
            tree = []
            for i in range(1, n + 1):
                k, l, r = map(int, input_data[i].split())
                tree.append(Node(k, l, r))

            result = "CORRECT" if is_bst(tree, 0, -2 ** 31, 2 ** 31 - 1) else "INCORRECT"

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_output)
        self.assertLess(execution_time, 10)
        self.assertLess(peak / 10 ** 6, 512)

    def test_bst_large_invalid(self):
        input_data = [
            "5",
            "10 1 2",
            "5 -1 -1",
            "8 -1 3",
            "15 -1 -1",
            "20 -1 -1"
        ]
        expected_output = "INCORRECT"

        start_time = time.time()
        tracemalloc.start()

        n = int(input_data[0].strip())
        if n == 0:
            result = "CORRECT"
        else:
            tree = []
            for i in range(1, n + 1):
                k, l, r = map(int, input_data[i].split())
                tree.append(Node(k, l, r))

            result = "CORRECT" if is_bst(tree, 0, -2 ** 31, 2 ** 31 - 1) else "INCORRECT"

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_output)
        self.assertLess(execution_time, 10)
        self.assertLess(peak / 10 ** 6, 512)

    def test_bst_empty(self):
        input_data = ["0"]
        expected_output = "CORRECT"

        start_time = time.time()
        tracemalloc.start()

        n = int(input_data[0].strip())
        if n == 0:
            result = "CORRECT"
        else:
            tree = []
            for i in range(1, n + 1):
                k, l, r = map(int, input_data[i].split())
                tree.append(Node(k, l, r))

            result = "CORRECT" if is_bst(tree, 0, -2 ** 31, 2 ** 31 - 1) else "INCORRECT"

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_output)
        self.assertLess(execution_time, 10)
        self.assertLess(peak / 10 ** 6, 512)


if __name__ == '__main__':
    unittest.main()
