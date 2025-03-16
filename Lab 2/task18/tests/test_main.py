import unittest
import time
import tracemalloc
from task18.src.main import build_rope, split, merge, traverse

class TestTask20(unittest.TestCase):

    def test_custom_case_with_performance(self):
        input_str = "xyzuvw"
        operations = [(1, 2, 3), (3, 5, 0)]
        expected_output = "yzwxuv"

        tracemalloc.start()
        start_time = time.perf_counter()

        root = build_rope(input_str)

        for i, j, k in operations:
            left, temp = split(root, i)
            mid, right = split(temp, j - i + 1)
            new_root = merge(left, right)
            left_part, right_part = split(new_root, k)
            root = merge(merge(left_part, mid), right_part)

        result = traverse(root)

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        execution_time = time.perf_counter() - start_time

        self.assertEqual(result, expected_output)
        self.assertLess(execution_time, 120)
        self.assertLess(peak / 10**6, 512)

    def test_large_case_with_performance(self):
        input_str = "abcdefghijklmno"
        operations = [(2, 5, 10), (0, 3, 7)]
        expected_output = "ijklmncabghdefo"

        tracemalloc.start()
        start_time = time.perf_counter()

        root = build_rope(input_str)

        for i, j, k in operations:
            left, temp = split(root, i)
            mid, right = split(temp, j - i + 1)
            new_root = merge(left, right)
            left_part, right_part = split(new_root, k)
            root = merge(merge(left_part, mid), right_part)

        result = traverse(root)

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        execution_time = time.perf_counter() - start_time

        self.assertEqual(result, expected_output)
        self.assertLess(execution_time, 120)
        self.assertLess(peak / 10 ** 6, 512)


if __name__ == '__main__':
    unittest.main()
