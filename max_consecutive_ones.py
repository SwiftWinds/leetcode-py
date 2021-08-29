from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        cur = 0
        for num in nums:
            if num == 1:
                cur += 1
            else:
                cur = 0
            if cur > max:
                max = cur
        return max
