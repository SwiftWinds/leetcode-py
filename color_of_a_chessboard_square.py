class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return int(coordinates[1]) % 2 == (ord(coordinates[0]) - ord('a')) % 2


assert not Solution().squareIsWhite("a1")
assert Solution().squareIsWhite("h3")
