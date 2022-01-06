from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        left = 0
        right = len(sorted_nums) - 1
        sum = sorted_nums[left] + sorted_nums[right]
        while sum != target:
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            sum = sorted_nums[left] + sorted_nums[right]
        return [nums.index(sorted_nums[left]), len(nums) - nums[::-1].index(sorted_nums[right]) - 1]
