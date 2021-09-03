from typing import List

from scipy.special import comb


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return [comb(rowIndex, i, exact=True) for i in range(rowIndex + 1)]


s = Solution()
assert s.getRow(3) == [1, 3, 3, 1]
