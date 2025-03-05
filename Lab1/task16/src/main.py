import time
import tracemalloc
from utils import read_file, write_file

t_start = time.perf_counter()

tracemalloc.start()

PATH = '../txtf/input.txt'
OUT_PATH = '../txtf/output.txt'


def Solve(n, distance):
    INF = float('inf')
    full_mask = (1 << n) - 1
    dp = [[INF] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]

    for i in range(n):
        dp[1 << i][i] = 0

    for mask in range(1 << n):
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v):
                    continue
                new_mask = mask | (1 << v)
                new_cost = dp[mask][u] + distance[u][v]
                if new_cost < dp[new_mask][v]:
                    dp[new_mask][v] = new_cost
                    parent[new_mask][v] = u

    result = INF
    city_end = -1

    for i in range(n):
        if dp[full_mask][i] < result:
            result = dp[full_mask][i]
            city_end = i

    arr = []
    mask = full_mask
    current = city_end

    for _ in range(n):
        arr.append(current)
        prev = parent[mask][current]
        if prev == -1:
            break
        mask ^= (1 << current)
        current = prev

    arr.reverse()
    arr = [x + 1 for x in arr]
    return result, arr


if __name__ == '__main__':
    input_data = read_file(PATH)
    data = list(map(int, input_data.strip().split()))

    n = data[0]
    distances = []
    for i in range(n):
        start = 1 + i * n
        end = start + n
        row = data[start:end]
        distances.append(row)
    result, arr = Solve(n, distances)
    write_file(OUT_PATH, f"{result}\n{' '.join(map(str, arr))}\n")

    print("Время 16 задания:", time.perf_counter() - t_start)
    print('Объем используемой памяти:', tracemalloc.get_traced_memory()[1], 'bytes')