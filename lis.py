from itertools import islice
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        T = [1] * len(nums)
        for i, num_i in enumerate(nums):
            for j, num_j in islice(enumerate(nums), i):
                if num_i > num_j and T[i] < T[j] + 1:
                    T[i] = T[j] + 1
        return max(T)
