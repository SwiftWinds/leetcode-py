from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        num_evens = 0
        num_odds = 0
        for i, pos in enumerate(position):
            if pos % 2:
                num_evens += 1
            else:
                num_odds += 1
        return min(num_evens, num_odds)


sol = Solution()
print(sol.minCostToMoveChips([1000000000]))
