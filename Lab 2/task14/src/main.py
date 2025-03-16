import time
import tracemalloc
from utils import read_file, write_file

t_start = time.perf_counter()
tracemalloc.start()

PATH = '../txtf/input.txt'
OUT_PATH = '../txtf/output.txt'


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


def get_height(node):
    return node.height if node else 0


def upd_height(node):
    if node:
        node.height = 1 + max(get_height(node.left), get_height(node.right))


def right_rotate(y):
    x = y.left
    Tr_2 = x.right
    x.right = y
    y.left = Tr_2
    upd_height(y)
    upd_height(x)
    return x


def left_rotate(x):
    y = x.right
    Tr_2 = y.left
    y.left = x
    x.right = Tr_2
    upd_height(x)
    upd_height(y)
    return y


def insert_node(node, value):
    if node is None:
        return Node(value)

    if value < node.value:
        node.left = insert_node(node.left, value)
    elif value > node.value:
        node.right = insert_node(node.right, value)
    else:
        return node

    upd_height(node)
    value_balance = get_height(node.left) - get_height(node.right)

    if value_balance > 1 and value < node.left.value:
        return right_rotate(node)
    if value_balance < -1 and value > node.right.value:
        return left_rotate(node)
    if value_balance > 1 and value > node.left.value:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    if value_balance < -1 and value < node.right.value:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node


def build_tree(nodes):
    if not nodes:
        return None

    node_dict = {}
    for idx, (value, left, right) in enumerate(nodes):
        node_dict[idx + 1] = Node(value)

    for idx, (value, left, right) in enumerate(nodes):
        current_node = node_dict[idx + 1]
        if left != 0:
            current_node.left = node_dict.get(left)
        if right != 0:
            current_node.right = node_dict.get(right)

    return node_dict.get(1)


def preorder(node, result):
    if node:
        result.append(node)
        preorder(node.left, result)
        preorder(node.right, result)


def format_output(root):
    preorder_nodes = []
    preorder(root, preorder_nodes)

    index_map = {node: i + 1 for i, node in enumerate(preorder_nodes)}

    output = [str(len(preorder_nodes))]
    for node in preorder_nodes:
        left_idx = index_map.get(node.left, 0)
        right_idx = index_map.get(node.right, 0)
        output.append(f"{node.value} {left_idx} {right_idx}")

    return "\n".join(output)


if __name__ == '__main__':
    input_data = read_file(PATH).splitlines()
    n = int(input_data[0])
    nodes = [tuple(map(int, line.split())) for line in input_data[1:n + 1]]
    x = int(input_data[n + 1])

    root = build_tree(nodes)
    root = insert_node(root, x)

    output_data = format_output(root)
    write_file(OUT_PATH, output_data)

    print("Время 14 задания:", time.perf_counter() - t_start)
    print('Объем используемой памяти:', tracemalloc.get_traced_memory()[1], 'bytes')

    # def insert_node(root, key):
    #     if root is None:
    #         return Node(key)  # Создаём новый корень