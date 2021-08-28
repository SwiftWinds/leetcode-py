from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def sub(nums, start, end, target):
            if start > end:
                return -1
            i = (start + end) // 2
            if nums[i] < target:
                return sub(nums, i + 1, end, target)
            elif nums[i] == target:
                return i
            else:
                return sub(nums, start, i - 1, target)

        return sub(nums, 0, len(nums) - 1, target)


sol = Solution()
assert sol.search(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4
assert sol.search(nums=[-1, 0, 3, 5, 9, 12], target=2) == -1
assert sol.search([2, 5], 2) == 0
