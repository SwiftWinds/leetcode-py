from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def subperm(taken, remaining, out):
            if len(remaining) == 0:
                res.append(out)
            else:
                for i, el in enumerate(remaining):
                    if el not in taken:
                        taken_copy = taken.copy()
                        remaining_copy = remaining.copy()
                        taken_copy.append(el)
                        del remaining_copy[i]
                        out_copy = out.copy()
                        out_copy.append(el)
                        subperm(taken_copy, remaining_copy, out_copy)

        out = []
        taken = []
        remaining = nums.copy()
        subperm(taken, remaining, out)

        return res


solution = Solution()
print(solution.permute([1, 2, 3]))
