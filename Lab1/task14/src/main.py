import time
import tracemalloc
from utils import read_file, write_file

t_start = time.perf_counter()

tracemalloc.start()

PATH = '../txtf/input.txt'
OUT_PATH = '../txtf/output.txt'


def calculate(a, b, operate):
    if operate == '+':
        return a + b
    elif operate == '-':
        return a - b
    elif operate == '*':
        return a * b

def Solve(expression):
    numbers = []
    operators = []
    for char in expression:
        if char.isdigit():
            numbers.append(int(char))
        else:
            operators.append(char)

    n = len(numbers)
    dp_max = [[0] * n for _ in range(n)]
    dp_min = [[0] * n for _ in range(n)]

    for i in range(n):
        dp_max[i][i] = numbers[i]
        dp_min[i][i] = numbers[i]

    for length in range(1, n):
        for i in range(n - length):
            j = i + length
            dp_max[i][j] = float('-inf')
            dp_min[i][j] = float('inf')

            for k in range(i, j):
                op = operators[k]

                a = calculate(dp_max[i][k], dp_max[k + 1][j], op)
                b = calculate(dp_max[i][k], dp_min[k + 1][j], op)
                c = calculate(dp_min[i][k], dp_max[k + 1][j], op)
                d = calculate(dp_min[i][k], dp_min[k + 1][j], op)

                dp_max[i][j] = max(dp_max[i][j], a, b, c, d)
                dp_min[i][j] = min(dp_min[i][j], a, b, c, d)

    return dp_max[0][n - 1]


if __name__ == '__main__':
    expression = read_file(PATH).strip()
    result = Solve(expression)
    write_file(OUT_PATH, f"{result}\n")
    print("Время 14 задания:", time.perf_counter() - t_start)
    print('Объем используемой памяти:', tracemalloc.get_traced_memory()[1], 'bytes')
