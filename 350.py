from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = Counter(nums1) & Counter(nums2)
        return list(nums.elements())
