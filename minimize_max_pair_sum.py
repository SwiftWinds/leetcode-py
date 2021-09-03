from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max = float("-inf")
        for i, el in enumerate(nums):
            if i > len(nums) // 2:
                break
            n = el + nums[-i - 1]
            if n > max:
                max = n

        return max
