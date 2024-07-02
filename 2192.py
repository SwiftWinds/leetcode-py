from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[v].append(u)
        ans = []
        for i in range(n):
            seen = set()

            def dfs(u):
                if u in seen:
                    return
                seen.add(u)
                for v in adj[u]:
                    dfs(v)

            for v in adj[i]:
                dfs(v)
            ans.append(sorted(list(seen)))
        return ans


if __name__ == "__main__":
    s = Solution()
    print(
        s.getAncestors(
            n=8,
            edges=[
                [0, 3],
                [0, 4],
                [1, 3],
                [2, 4],
                [2, 7],
                [3, 5],
                [3, 6],
                [3, 7],
                [4, 6],
            ],
        )
    )  # [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
    print(
        s.getAncestors(
            n=5,
            edges=[
                [0, 1],
                [0, 2],
                [0, 3],
                [0, 4],
                [1, 2],
                [1, 3],
                [1, 4],
                [2, 3],
                [2, 4],
                [3, 4],
            ],
        )
    )  # [[],[0],[0,1],[0,1,2],[0,1,2,3]]
