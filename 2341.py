from typing import List
from collections import Counter

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        p = l = 0
        for f in c.values():
            p += f // 2
            l += f % 2
        return [p, l]