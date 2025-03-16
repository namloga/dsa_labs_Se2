import time
import tracemalloc
from utils import read_file, write_file

t_start = time.perf_counter()
tracemalloc.start()

PATH = '../txtf/input.txt'
OUT_PATH = '../txtf/output.txt'

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.size = 1

def update_size(node):
    if node:
        node.size = 1 + (node.left.size if node.left else 0) + (node.right.size if node.right else 0)


def insert(root,k):
    if root is None:
        return Node(k)

    current = root
    arr = []

    while True:
        arr.append(current)
        if k < current.key:
            if current.left is None:
                current.left = Node(k)
                break
            current = current.left
        elif k > current.key:
            if current.right is None:
                current.right = Node(k)
                break
            current = current.right
        else:
            return root

    for node in reversed(arr):
        update_size(node)

    return root


def find_k(root, k):
    if root is None or k < 1:
        return None

    current = root

    while current:
        left_size = current.left.size if current.left else 0
        if k <= left_size:
            current = current.left
        elif k == left_size + 1:
            return current.key
        else:
            k -= left_size + 1
            current = current.right

    return None


if __name__ == "__main__":
    root = None
    result = []
    input_data = read_file(PATH).splitlines()

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

    write_file(OUT_PATH, "\n".join(result))

    print("Время 4 задания:", time.perf_counter() - t_start)
    print('Объем используемой памяти:', tracemalloc.get_traced_memory()[1], 'bytes')
