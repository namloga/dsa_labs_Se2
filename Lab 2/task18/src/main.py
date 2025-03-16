import time
import tracemalloc
from utils import read_file, write_file
import random

t_start = time.perf_counter()
tracemalloc.start()

PATH = '../txtf/input.txt'
OUT_PATH = '../txtf/output.txt'


class Node:
    __slots__ = ('val', 'priority', 'left', 'right', 'size')

    def __init__(self, val):
        self.val = val
        self.priority = random.randrange(1 << 30)
        self.left = None
        self.right = None
        self.size = 1


def upd_size(node):
    if node:
        node.size = 1
        if node.left:
            node.size += node.left.size
        if node.right:
            node.size += node.right.size


def split(node, count):
    if node is None or count <= 0:
        return (None, node)
    if count >= node.size:
        return (node, None)

    left_size = node.left.size if node.left else 0
    if count <= left_size:
        left, node.left = split(node.left, count)
        upd_size(node)
        return (left, node)
    else:
        node.right, right = split(node.right, count - left_size - 1)
        upd_size(node)
        return (node, right)


def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left

    if left.priority > right.priority:
        left.right = merge(left.right, right)
        upd_size(left)
        return left
    else:
        right.left = merge(left, right.left)
        upd_size(right)
        return right


def build_rope(s):
    root = None
    for ch in s:
        root = merge(root, Node(ch))
    return root


def traverse(root):
    result = []
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            result.append(node.val)
            node = node.right
    return ''.join(result)

if __name__ == '__main__':
    input_data = read_file(PATH).splitlines()
    if not input_data:
        write_file(OUT_PATH, "")
    else:
        s = input_data[0]
        n = int(input_data[1]) if len(input_data) > 1 else 0
        queries = [tuple(map(int, line.split())) for line in input_data[2:2 + n]]

        root = build_rope(s)

        for i, j, k in queries:
            left, temp = split(root, i)
            mid, right = split(temp, j - i + 1)

            new_root = merge(left, right)

            left_part, right_part = split(new_root, k)
            root = merge(merge(left_part, mid), right_part)

        result = traverse(root)
        write_file(OUT_PATH, result)

    print("Время 18 задания:", time.perf_counter() - t_start)
    print('Объем используемой памяти:', tracemalloc.get_traced_memory()[1], 'bytes')