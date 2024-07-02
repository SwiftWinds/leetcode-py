from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for u, v in roads:
            adj[u].append(v)
            adj[v].append(u)
        adj = dict(sorted(adj.items(), key=lambda x: len(x[1])))
        importance = [0] * n
        for idx, (u, _) in enumerate(adj.items()):
            importance[u] = idx + 1
        tot = 0
        for u, v in roads:
            tot += importance[u] + importance[v]
        return tot


if __name__ == "__main__":
    print(
        Solution().maximumImportance(
            5, [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
        )
    )  # 43
    print(Solution().maximumImportance(n=5, roads=[[0, 3], [2, 4], [1, 3]]))  # 20
