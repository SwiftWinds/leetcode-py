from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        i = 0
        while i + 2 < len(nums):
            if nums[i] >= nums[i + 1] + nums[i + 2]:
                i += 1
            else:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0


sol = Solution()
assert sol.largestPerimeter([1, 2, 1]) == 0
