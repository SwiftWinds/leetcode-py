from typing import List
from collections import defaultdict


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for a, b in adjacentPairs:
            adj[a].append(b)
            adj[b].append(a)

        for v, neighbors in adj.items():
            if len(neighbors) == 1:
                s = v
                break
        
        res = [s]
        p = s
        v = adj[p][0]
        while len(adj[v]) > 1:
            res.append(v)
            v, p = adj[v][0] if adj[v][0] != p else adj[v][1], v
        res.append(v)
        return res


print(Solution().restoreArray([[2, 1], [3, 4], [3, 2]]))
print(Solution().restoreArray([[4, -2], [1, 4], [-3, 1]]))
