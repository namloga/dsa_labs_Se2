import time
import tracemalloc
from utils import read_file, write_file

t_start = time.perf_counter()

tracemalloc.start()

PATH = '../txtf/input.txt'
OUT_PATH = '../txtf/output.txt'

def Solve(n, W, items):
    arr = []
    for item in items:
        p, w = item[0], item[1]
        if w > 0:
            arr.append((p, w, p / w))

    arr.sort(key=lambda x: x[2], reverse=True)
    max_value = 0.0

    for p, w, v in arr:
        if W >= w:
            max_value += p
            W -= w
        else:
            max_value += v * W
            break

    return format(max_value, ".4f")

if __name__ == '__main__':
    data = read_file(PATH).strip().split("\n")
    n, W = map(int, data[0].split())
    items = []
    for i in range(1, n + 1):
        p, w = map(int, data[i].split())
        items.append([p,w])
    result = Solve(n, W, items)
    write_file(OUT_PATH, f"{result}\n")
    print("Время 1 задания:", time.perf_counter() - t_start)
    print('Объем используемой памяти:', tracemalloc.get_traced_memory()[1], 'bytes')
