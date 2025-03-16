import time
import tracemalloc
from utils import read_file, write_file

t_start = time.perf_counter()
tracemalloc.start()

PATH = '../txtf/input.txt'
OUT_PATH = '../txtf/output.txt'

class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

def is_bst(tree, index, min_val, max_val):
    if index == -1:
        return True

    node = tree[index]

    if not (min_val <= node.key <= max_val):
        return False

    return (is_bst(tree, node.left, min_val, node.key - 1) and is_bst(tree, node.right, node.key, max_val))

if __name__ == "__main__":
    input_data = read_file(PATH).splitlines()
    n = int(input_data[0].strip())

    if n == 0:
        write_file(OUT_PATH, "CORRECT")
    else:
        tree = []
        for i in range(1, n + 1):
            k, l, r = map(int, input_data[i].split())
            tree.append(Node(k, l, r))

        result = "CORRECT" if is_bst(tree, 0, -2 ** 31, 2 ** 31 - 1) else "INCORRECT"
        write_file(OUT_PATH, result)

    print("Время 7 задания:", time.perf_counter() - t_start)
    print('Объем используемой памяти:', tracemalloc.get_traced_memory()[1], 'bytes')