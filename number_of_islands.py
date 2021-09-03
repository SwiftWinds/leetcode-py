from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        def sub(r, c):
            if (r, c) in visited:
                return
            height, width = len(grid), len(grid[0])
            if (r < 0 or r >= height) or (c < 0 or c >= width):
                return
            if grid[r][c] == "1":
                visited.add((r, c))
            else:
                return
            sub(r - 1, c)
            sub(r + 1, c)
            sub(r, c + 1)
            sub(r, c - 1)

        count = 0
        for i, row in enumerate(grid):
            for j, el in enumerate(row):
                if el == "1" and (i, j) not in visited:
                    sub(i, j)
                    count += 1
        return count


s = Solution()
assert s.numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3
