from math import sqrt, ceil
from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        guess = ceil(sqrt(area))
        while area % guess != 0:
            guess += 1
        return [guess, area // guess]
