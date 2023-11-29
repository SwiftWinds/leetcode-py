class Solution:
    def countHomogenous(self, s: str) -> int:
        p = s[0]
        ct = 1
        t = 0
        for c in s[1:]:
            if p != c:
                t += ct * (ct + 1) // 2
                p = c
                ct = 1
            else:
                ct += 1
        t += ct * (ct + 1) // 2
        return t % (10 ** 9 + 7)
