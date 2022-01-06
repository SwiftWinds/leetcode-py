from collections import deque
from itertools import zip_longest


def solution(A, B):
    overflow = deque([0, 0, 0])
    result = deque()
    for a, b in zip_longest(A, B, fillvalue=0):
        res = a + b + overflow[0]
        if res == 4:
            overflow[2] += 1
            result.append(0)
        elif res == 3 or res == 2:
            overflow[1] += 1
            overflow[2] += 1
            result.append(res - 2)
        else:
            result.append(res)
        overflow.popleft()
        overflow.append(0)
    if overflow[0] == 1:
        result.extend(overflow)
    while result[-1] == 0:
        result.pop()
    return list(result)


print(solution([1] * 100000, [1] * 100000))
