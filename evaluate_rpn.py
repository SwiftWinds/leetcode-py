from collections import deque
from math import trunc
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = deque()
        for token in tokens:
            try:
                s.append(int(token))
            except ValueError:
                r = s.pop()
                l = s.pop()
                if token == "+":
                    s.append(l + r)
                elif token == "-":
                    s.append(l - r)
                elif token == "*":
                    s.append(l * r)
                elif token == "/":
                    s.append(trunc(l / r))
        return s.pop()


s = Solution()
assert s.evalRPN(tokens=["4", "13", "5", "/", "+"]) == 6
assert s.evalRPN(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
