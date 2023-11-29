from typing import List
from math import gcd

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        d = gcd(*numsDivide)
        nums.sort()
        t = 0
        for n in nums:
            if d % n == 0:
                return t
            t += 1
        return -1