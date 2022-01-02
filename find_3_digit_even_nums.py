from typing import List

from sortedcontainers import SortedSet


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        """
        Returns a sorted list of 3-digit even numbers from list of digits
        """

        def generate_headers(nums: List[int]) -> List[int]:
            prev_first_digit = float("nan")
            headers = []
            for i, first_digit in enumerate(nums):
                if first_digit != prev_first_digit and first_digit != 0:
                    prev_first_digit = first_digit
                    prev_second_digit = float("nan")
                    for j, second_digit in enumerate(nums):
                        if second_digit != prev_second_digit and i != j:
                            headers.append(first_digit * 10 + second_digit)
            return headers

        digits.sort()
        even_nums = SortedSet()
        last_even = float("nan")
        for i, digit in enumerate(digits):
            if digit != last_even and digit % 2 == 0:
                last_even = digit
                digits_without_i = digits[:i] + digits[i + 1:]
                headers = generate_headers(digits_without_i)
                even_nums.update([header * 10 + digit for header in headers])
        return list(even_nums)
