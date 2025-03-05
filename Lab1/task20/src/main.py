import time
import tracemalloc
from utils import read_file, write_file

t_start = time.perf_counter()

tracemalloc.start()

PATH = '../txtf/input.txt'
OUT_PATH = '../txtf/output.txt'

def Solve(n, k, s):
    count = 0

    for middle in range(n):
        left, right = middle, middle
        matches = 0

        while left >= 0 and right < n:
            if s[left] != s[right]:
                matches += 1
            if matches > k:
                break
            count += 1
            left -= 1
            right += 1

        left, right = middle, middle + 1
        matches = 0

        while left >= 0 and right < n:
            if s[left] != s[right]:
                matches += 1
            if matches > k:
                break
            count += 1
            left -= 1
            right += 1

    return count

if __name__ == '__main__':
    input_data = read_file(PATH).strip().split("\n")
    n, k = map(int, input_data[0].split())
    s = input_data[1].strip()
    result = Solve(n, k, s)
    write_file(OUT_PATH, f"{result}\n")
    print("Время 20 задания:", time.perf_counter() - t_start)
    print('Объем используемой памяти:', tracemalloc.get_traced_memory()[1], 'bytes')
