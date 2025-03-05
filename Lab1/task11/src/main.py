import time
import tracemalloc
from utils import read_file, write_file

t_start = time.perf_counter()

tracemalloc.start()

PATH = '../txtf/input.txt'
OUT_PATH = '../txtf/output.txt'

def Solve(W, weights):
    if W == 0:
        return 0
    weights_valid = [w for w in weights if 0 < w <= W]
    dp = [0] * (W + 1)
    for w in weights_valid:
        for j in range(W, w - 1, -1):
            dp[j] = max(dp[j], dp[j - w] + w)
    return dp[W]

if __name__ == '__main__':
    input_data = read_file(PATH)
    data = list(map(int, input_data.strip().split()))
    W = data[0]
    weights = data[2:]
    result = Solve(W, weights)
    write_file(OUT_PATH, f"{result}\n")
    print("Время 11 задания:", time.perf_counter() - t_start)
    print('Объем используемой памяти:', tracemalloc.get_traced_memory()[1], 'bytes')
