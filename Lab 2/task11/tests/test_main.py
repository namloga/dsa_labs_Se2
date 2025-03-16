import unittest
import tracemalloc
import time
from task11.src.main import insert, delete, exists, next_value, prev_value, Node

class TestTask11(unittest.TestCase):

    def test_treap_operations(self):
        input_data = [
            "insert 10", "insert 20", "insert 5", "insert 15", "insert 25",
            "exists 10", "exists 30", "exists 5",
            "next 10", "next 15", "next 25", "next 30",
            "prev 20", "prev 5", "prev 3",
            "delete 10", "exists 10", "next 5", "prev 15"
        ]

        expected_output = [
            "true", "false", "true",
            "15", "20", "none", "none",
            "15", "none", "none",
            "false", "15", "5"
        ]

        start_time = time.time()
        tracemalloc.start()

        root = None
        result = []

        for line in input_data:
            command = line.split()
            if not command:
                continue

            op = command[0]
            x = int(command[1])

            if op == "insert":
                root = insert(root, x)
            elif op == "delete":
                root = delete(root, x)
            elif op == "exists":
                result.append("true" if exists(root, x) else "false")
            elif op == "next":
                value = next_value(root, x)
                result.append(str(value) if value is not None else "none")
            elif op == "prev":
                value = prev_value(root, x)
                result.append(str(value) if value is not None else "none")

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_output)
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10 ** 6, 512)

    def test_treap_complex_operations(self):
        input_data = [
            "insert 50", "insert 30", "insert 70", "insert 20", "insert 40",
            "insert 60", "insert 80", "insert 35", "insert 45", "insert 55",
            "insert 65", "insert 75", "insert 85", "insert 30", "insert 40",
            "exists 50", "exists 90", "exists 40", "exists 35",
            "next 30", "next 50", "next 85", "next 90",
            "prev 60", "prev 40", "prev 15",
            "delete 50", "delete 30", "exists 50", "exists 30",
            "next 40", "prev 60"
        ]

        expected_output = [
            "true", "false", "true", "true",
            "35", "55", "none", "none",
            "55", "35", "none",
            "false", "false",
            "45", "55"
        ]

        start_time = time.time()
        tracemalloc.start()

        root = None
        result = []

        for line in input_data:
            command = line.split()
            if not command:
                continue

            op = command[0]
            x = int(command[1])

            if op == "insert":
                root = insert(root, x)
            elif op == "delete":
                root = delete(root, x)
            elif op == "exists":
                result.append("true" if exists(root, x) else "false")
            elif op == "next":
                value = next_value(root, x)
                result.append(str(value) if value is not None else "none")
            elif op == "prev":
                value = prev_value(root, x)
                result.append(str(value) if value is not None else "none")

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        execution_time = end_time - start_time

        self.assertEqual(result, expected_output)
        self.assertLess(execution_time, 2)
        self.assertLess(peak / 10 ** 6, 512)


if __name__ == '__main__':
    unittest.main()
