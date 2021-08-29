from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = None
        cur_sum = None
        for num in nums:
            if cur_sum is None or cur_sum < 0:
                cur_sum = num
            else:
                cur_sum += num
            if max_sum is None or cur_sum > max_sum:
                max_sum = cur_sum

        return max_sum


sol = Solution()
assert sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert sol.maxSubArray([1]) == 1
assert sol.maxSubArray([5, 4, -1, 7, 8]) == 23
assert sol.maxSubArray([-2, 1]) == 1
assert sol.maxSubArray([-2, -1]) == -1
