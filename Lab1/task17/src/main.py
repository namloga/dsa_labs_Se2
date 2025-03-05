import time
import tracemalloc
from utils import read_file, write_file

t_start = time.perf_counter()

tracemalloc.start()

PATH = '../txtf/input.txt'
OUT_PATH = '../txtf/output.txt'

def Solve(N):
    MOD = 10**9
    moves = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4]
    }
    dp = [0] * 10

    for i in range(10):
        dp[i] = 1 if i not in (0, 8) else 0

    for _ in range(1, N):
        new_dp = [0] * 10
        for j in range(10):
            if dp[j] == 0:
                continue
            for next in moves[j]:
                new_dp[next] = (new_dp[next] + dp[j]) % MOD
        dp = new_dp

    return sum(dp) % MOD

if __name__ == '__main__':
    N = int(read_file(PATH).strip())
    result = Solve(N)
    write_file(OUT_PATH, f"{result}\n")
    print("Время 17 задания:", time.perf_counter() - t_start)
    print('Объем используемой памяти:', tracemalloc.get_traced_memory()[1], 'bytes')
