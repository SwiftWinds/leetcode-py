from math import sqrt, ceil


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum = 0
        for i in range(1, ceil(sqrt(num))):
            if num % i == 0:
                if i != num:
                    sum += i
                if num // i != num:
                    sum += num // i
        return sum == num


sol = Solution()
assert sol.checkPerfectNumber(28)
