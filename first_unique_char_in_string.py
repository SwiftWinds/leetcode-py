a_ord = ord('a')


class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = [[] for _ in range(26)]
        for i, ch in enumerate(s):
            idx = ord(ch) - a_ord
            chars[idx].append(i)
        uniques = list(filter(lambda char: len(char) == 1, chars))
        if len(uniques) == 0:
            return -1
        sorted_uniques = sorted(uniques, key=lambda char: char[0])
        return sorted_uniques[0][0]
