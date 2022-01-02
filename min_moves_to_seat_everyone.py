from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        sum = 0
        for seat, student in zip(seats, students):
            sum += abs(seat - student)
        return sum
