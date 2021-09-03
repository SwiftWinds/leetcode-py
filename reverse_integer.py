class Solution:
    def reverse(self, x: int) -> int:
        r = str(x)[::-1]
        if r[-1] == "-":
            n = -int(r[:-1])
        else:
            n = int(r)
        if n > 2 ** 31 - 1 or n < -2 ** 31:
            return 0
        return n
