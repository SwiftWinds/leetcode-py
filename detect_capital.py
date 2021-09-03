class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.islower() or word.isupper() or word.istitle()


s = Solution()
assert s.detectCapitalUse("USA")
assert not s.detectCapitalUse("FlaG")
