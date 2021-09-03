from collections import deque
from dataclasses import dataclass


@dataclass
class StockSpanner:
    s = deque()

    def next(self, price: int) -> int:
        today = [price, 1]
        prev = self.s[-1]
        while self.s and prev[0] <= today:
            self.s.pop()


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
assert obj.next(85)
assert obj.next(100) == 1
assert obj.next(80) == 1
assert obj.next(60) == 1
assert obj.next(70) == 2
