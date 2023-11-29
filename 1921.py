from typing import List

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        ld = [-(-start//vel) for start, vel in zip(dist, speed)]
        ld.sort()
        n = 0
        for i in range(len(ld)):
            if ld[i] < i + 1:
                return n
            n += 1
        return n