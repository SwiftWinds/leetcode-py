from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        a_ascii = ord("a")
        order_map = {}
        for i, ch in enumerate(order):
            order_map[ch] = i
        reordered_words = []
        for word in words:
            s = ""
            for ch in word:
                offset = order_map[ch]
                s += chr(a_ascii + offset)
            reordered_words.append(s)
        return reordered_words == sorted(reordered_words)


s = Solution()
assert s.isAlienSorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz")
assert not s.isAlienSorted(words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz")
assert not s.isAlienSorted(words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz")
