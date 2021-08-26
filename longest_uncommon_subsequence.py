from collections import Counter
from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        d = {}
        for str in strs:
            if len(str) not in d:
                d[len(str)] = []
            d[len(str)].append(str)
        longest = d[max(d, key=int)]
        occs = Counter(strs)
        uniques = list(map(lambda pair: pair[0], filter(lambda pair: pair[1] == 1, occs.items())))
        sorted_uniques = list(reversed(sorted(uniques, key=len)))
        if len(sorted_uniques) == 0:
            return -1
        if len(sorted_uniques[0]) == len(longest[0]):
            return len(sorted_uniques[0])
        for sorted_unique in sorted_uniques:
            def is_subsequence(sub, longest_strs):
                for str in longest_strs:
                    cur = 0
                    for ch in str:
                        if sub[cur] == ch:
                            cur += 1
                            if cur == len(sub):
                                return True
                return False

            if not is_subsequence(sorted_unique, longest):
                return len(sorted_unique)

        return -1


sol = Solution()
print(sol.findLUSlength(["aaaaa", "aaaaa", "aaa", "aaa"]))
