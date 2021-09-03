from math import gcd, floor, sqrt


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        divisors = set()
        g = gcd(len(str1), len(str2))
        divisors.add(g)
        for i in range(1, floor(sqrt(g)) + 1):
            if g % i == 0:
                divisors.update([i, g // i])
        divisors = list(divisors)
        divisors.sort(reverse=True)

        def divides(sub, str):
            for i, actual in enumerate(str):
                expected = sub[i % len(sub)]
                if actual != expected:
                    return False
            return True

        for divisor in divisors:
            divisor_str = str1[:divisor]
            if divides(divisor_str, str1) and divides(divisor_str, str2):
                return divisor_str
        return ""


sol = Solution()
assert sol.gcdOfStrings("abababab", "abab") == "abab"
