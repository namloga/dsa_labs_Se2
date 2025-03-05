import time
import tracemalloc
from utils import read_file, write_file

t_start = time.perf_counter()

tracemalloc.start()

PATH = '../txtf/input.txt'
OUT_PATH = '../txtf/output.txt'

def Solve(s):
    stack = []
    marks_invalid = set()
    pairs = {')': '(', ']': '[', '}': '{'}
    open_marks = "([{"
    close_marks = ")]}"

    for i, char in enumerate(s):
        if char in open_marks:
            stack.append(i)
        elif char in close_marks:
            if stack and s[stack[-1]] == pairs[char]:
                stack.pop()
            else:
                marks_invalid.add(i)

    marks_invalid.update(stack)
    result = []
    k = "()[]{}"

    for i, char in enumerate(s):
        if char not in k:
            result.append(char)
        elif i not in marks_invalid:
            result.append(char)

    return ''.join(result)

if __name__ == '__main__':
    s = read_file(PATH).strip()
    result = Solve(s)
    write_file(OUT_PATH, f"{result}\n")
    print("Время 15 задания:", time.perf_counter() - t_start)
    print('Объем используемой памяти:', tracemalloc.get_traced_memory()[1], 'bytes')
