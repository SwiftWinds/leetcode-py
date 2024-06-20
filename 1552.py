from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        lhop = 1
        rhop = (position[-1] - position[0]) // (m - 1)
        mhop = (lhop + rhop) // 2
        best = 0
        while lhop <= rhop:
            mhop = (lhop + rhop) // 2
            prev = position[0]
            count = 1
            j = 1
            while count < m and j < n:
                if position[j] >= prev + mhop:
                    count += 1
                    prev = position[j]
                if count < m:
                    j += 1
            if j == n:
                rhop = mhop - 1
            else:
                best = mhop
                lhop = mhop + 1
        return best
    
if __name__ == "__main__":
    print(Solution().maxDistance([1, 2, 3, 4, 7], 3))  # 3
    print(Solution().maxDistance([5, 4, 3, 2, 1, 1000000000], 2))  # 999999999
