import time
import tracemalloc
from utils import read_file, write_file
import sys, random

t_start = time.perf_counter()
tracemalloc.start()

PATH = '../txtf/input.txt'
OUT_PATH = '../txtf/output.txt'


class Node:
    __slots__ = ('key', 'priority', 'left', 'right')

    def __init__(self, key):
        self.key = key
        self.priority = random.randint(1, 10**9)
        self.left = None
        self.right = None


def split_tree(node, key):
    if node is None:
        return None, None

    if key > node.key:
        right_tree_left, right_tree = split_tree(node.right, key)
        node.right = right_tree_left
        return node, right_tree
    else:
        left_tree, right_tree_right = split_tree(node.left, key)
        node.left = right_tree_right
        return left_tree, node


def merge(left_node, right_node):
    if not left_node:
        return right_node
    if not right_node:
        return left_node

    if left_node.priority > right_node.priority:
        left_node.right = merge(left_node.right, right_node)
        return left_node
    else:
        right_node.left = merge(left_node, right_node.left)
        return right_node


def insert(root, key):
    left_tree, right_tree = split_tree(root, key)
    new_node = Node(key)
    return merge(merge(left_tree, new_node), right_tree)


def delete(root, key):
    left_tree, mid_tree = split_tree(root, key)
    mid_tree, right_tree = split_tree(mid_tree, key + 1)
    return merge(left_tree, right_tree)


def exists(root, key):
    while root:
        if key == root.key:
            return True
        elif key < root.key:
            root = root.left
        else:
            root = root.right
    return False


def next_value(root, key):
    x = None
    while root:
        if root.key > key:
            x = root.key
            root = root.left
        else:
            root = root.right
    return x


def prev_value(root, key):
    x = None
    while root:
        if root.key < key:
            x = root.key
            root = root.right
        else:
            root = root.left
    return x


if __name__ == '__main__':
    input_data = read_file(PATH).splitlines()

    root = None
    results = []

    for line in input_data:
        command = line.split()
        if not command:
            continue

        operate = command[0]
        x = int(command[1])

        if operate == "insert":
            root = insert(root, x)
        elif operate == "delete":
            root = delete(root, x)
        elif operate == "exists":
            results.append("true" if exists(root, x) else "false")
        elif operate == "next":
            value = next_value(root, x)
            results.append(str(value) if value is not None else "none")
        elif operate == "prev":
            value = prev_value(root, x)
            results.append(str(value) if value is not None else "none")

    write_file(OUT_PATH, "\n".join(results))

    print("Время 11 задания:", time.perf_counter() - t_start)
    print('Объем используемой памяти:', tracemalloc.get_traced_memory()[1], 'bytes')


    # def range_query(root, L, R, result):
    #     if root is None:
    #         return
    #     if L <= root.key <= R:
    #         range_query(root.left, L, R, result)
    #         result.append(root.key)
    #         range_query(root.right, L, R, result)
    #     elif root.key < L:
    #         range_query(root.right, L, R, result)
    #     else:
    #         range_query(root.left, L, R, result)

