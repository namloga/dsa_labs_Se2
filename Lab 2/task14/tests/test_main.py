import unittest
import tracemalloc
import time
from task14.src.main import build_tree, insert_node, format_output

class TestAVLTree(unittest.TestCase):

    def test_avl_basic_insert(self):
        input_nodes = [
            (10, 0, 0),
            (20, 1, 0),
            (30, 2, 0)
        ]
        x = 25

        expected_output = """
2
10 0 2
25 0 0"""

        tracemalloc.start()
        start_time = time.perf_counter()

        root = build_tree(input_nodes)
        root = insert_node(root, x)
        result = format_output(root)

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        execution_time = time.perf_counter() - start_time

        self.assertEqual(result.strip(), expected_output.strip())
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10**6, 512)

    def test_avl_large_insert(self):
        input_nodes = [
            (50, 0, 0),
            (30, 0, 0),
            (70, 0, 0),
            (20, 0, 0),
            (40, 0, 0),
            (60, 0, 0),
            (80, 0, 0)
        ]
        x = 55
        expected_output = """
2
50 0 2
55 0 0"""

        tracemalloc.start()
        start_time = time.perf_counter()

        root = build_tree(input_nodes)
        root = insert_node(root, x)
        result = format_output(root)

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        execution_time = time.perf_counter() - start_time

        self.assertEqual(result.strip(), expected_output.strip())
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10**6, 256)

    def test_avl_balance_after_insert(self):
        input_nodes = [
            (10, 0, 0),
            (20, 1, 0),
            (30, 2, 0),
            (40, 3, 0)
        ]
        x = 25
        expected_output = """
2
10 0 2
25 0 0"""

        tracemalloc.start()
        start_time = time.perf_counter()

        root = build_tree(input_nodes)
        root = insert_node(root, x)
        result = format_output(root)

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        execution_time = time.perf_counter() - start_time

        self.assertEqual(result.strip(), expected_output.strip())
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10**6, 256)

    def test_avl_insert_duplicate(self):
        input_nodes = [
            (15, 0, 0),
            (10, 0, 0),
            (20, 0, 0)
        ]
        x = 10
        expected_output = """
2
15 2 0
10 0 0"""

        tracemalloc.start()
        start_time = time.perf_counter()

        root = build_tree(input_nodes)
        root = insert_node(root, x)
        result = format_output(root)

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        execution_time = time.perf_counter() - start_time

        self.assertEqual(result.strip(), expected_output.strip())
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10**6, 256)

if __name__ == '__main__':
    unittest.main()
