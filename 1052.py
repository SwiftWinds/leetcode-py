from typing import List


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        ps = [0] * len(customers)
        psg = [0] * len(customers)
        for i in range(len(customers)):
            prev = 0 if i == 0 else ps[i - 1]
            prevg = 0 if i == 0 else psg[i - 1]
            ps[i] = prev + customers[i]
            psg[i] = prevg + customers[i] * -(grumpy[i] - 1)
        maxs = 0
        t = psg[-1]
        for i in range(len(customers) - minutes + 1):
            plus = ps[i + minutes - 1] - ps[i - 1] if i > 0 else ps[i + minutes - 1]
            minus = psg[i + minutes - 1] - psg[i - 1] if i > 0 else psg[i + minutes - 1]
            maxs = max(maxs, t - minus + plus)
        return maxs


if __name__ == "__main__":
    print(
        Solution().maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3)
    )  # 16
    print(Solution().maxSatisfied([1], [0], 1))  # 1
    print(Solution().maxSatisfied([1], [1], 1))  # 1
