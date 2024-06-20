from typing import List
import bisect

class Solution:
    def check_sol(self, bloom_day: List[int], m: int, k: int, d: int) -> bool:
        bouquets = 0
        consecutive = 0
        for bd in bloom_day:
            if bd <= d:
                consecutive += 1
                if consecutive == k:
                    bouquets += 1
                    consecutive = 0
                    if bouquets == m:
                        return True
            else:
                consecutive = 0
        return False

    def minDays(self, bloom_day: List[int], m: int, k: int) -> int:
        if m * k > len(bloom_day):
            return -1
        
        days = sorted(set(bloom_day))
        
        def condition(d):
            return self.check_sol(bloom_day, m, k, d)
        
        index = bisect.bisect_left(days, True, key=condition)
        
        return days[index] if index < len(days) else -1

if __name__ == "__main__":
    print(Solution().minDays([1, 10, 3, 10, 2], 3, 1))
    print(Solution().minDays([1, 10, 3, 10, 2], 3, 2))
    print(Solution().minDays([7, 7, 7, 7, 12, 7, 7], 2, 3))