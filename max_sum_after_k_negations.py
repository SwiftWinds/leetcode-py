from typing import List

import numpy as np


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()

        for i, num in enumerate(nums):
            if num < 0 < k:
                nums[i] = -num
                k -= 1
            else:
                break
        if k % 2 != 0:
            i = np.argmin(nums)
            nums[i] = -nums[i]
        return sum(nums)


assert Solution().largestSumAfterKNegations([-8, 3, -5, -3, -5, -2], 6) == 22
