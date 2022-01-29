from collections import Counter
from itertools import repeat
from typing import List

from sortedcontainers import SortedSet, SortedDict


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        sd = SortedDict()
        res = []
        for item, frequency in c.items():
            if frequency not in sd:
                sd[frequency] = SortedSet()
            sd[frequency].add(item)
        for frequency, items in sd.items():
            for item in reversed(items):
                res.extend(repeat(item, frequency))
        return res


assert Solution().frequencySort([-1, 1, -6, 4, 5, -6, 1, 4, 1]) == [5, -1, 4, 4, -6, -6, 1, 1, 1]
