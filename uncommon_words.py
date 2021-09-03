from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c = Counter(f"{s1} {s2}".split(" "))
        return [w for w in c if c[w] == 1]


s = Solution()
assert s.uncommonFromSentences("this apple is sweet", "this apple is sour") == ["sweet", "sour"]
assert s.uncommonFromSentences("s z z z s", "s z ejt") == ["ejt"]
