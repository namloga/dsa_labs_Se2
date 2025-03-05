import time
import tracemalloc
from utils import read_file, write_file

t_start = time.perf_counter()

tracemalloc.start()

PATH = '../txtf/input.txt'
OUT_PATH = '../txtf/output.txt'

def Solve(n):
    result = []
    sum_far = 0
    current = 1

    while sum_far + current <= n:
        result.append(current)
        sum_far += current
        current += 1

    result[-1] += (n - sum_far)

    return len(result), result

if __name__ == '__main__':
    input_data = read_file(PATH).strip()
    n = int(input_data)
    result, l = Solve(n)
    write_file(OUT_PATH, f"{result}\n{' '.join(map(str,l))}")
    print("Время 5 задания:", time.perf_counter() - t_start)
    print('Объем используемой памяти:', tracemalloc.get_traced_memory()[1], 'bytes')
