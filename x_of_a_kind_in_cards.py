from collections import Counter
from math import gcd
from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        c = Counter(deck)
        num_appearances = list(c.values())
        return gcd(*num_appearances) >= 2
