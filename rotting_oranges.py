from typing import List

import numpy as np


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        dp = [[0 if grid[i][j] == 0 else float("inf") for j in range(m)] for i in range(n)]

        in_range = lambda i, j: 0 <= i < n and 0 <= j < m

        is_empty = lambda i, j: grid[i][j] == 0

        def sub(i, j, age):
            if not in_range(i, j):
                return
            if is_empty(i, j):
                dp[i][j] = 0
                return
            if dp[i][j] <= age:
                return
            dp[i][j] = age

            sub(i + 1, j, age + 1)
            sub(i - 1, j, age + 1)
            sub(i, j + 1, age + 1)
            sub(i, j - 1, age + 1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    sub(i, j, 0)
        return -1 if np.amax(dp) == float('inf') else np.amax(dp)


s = Solution()
assert s.orangesRotting([[0]]) == 0
