from math import ceil, floor


class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n > 1:
            matches += floor(n / 2)
            n = ceil(n / 2)
        return matches


s = Solution()
assert s.numberOfMatches(7) == 6
assert s.numberOfMatches(14) == 13
