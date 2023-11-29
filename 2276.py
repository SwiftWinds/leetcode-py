from sortedcontainers import SortedList


class CountIntervals:
    def __init__(self):
        self.c = 0
        self.s = SortedList()
        self.stoe = {}
        self.e = SortedList()
        self.etos = {}

    def remove(self, left: int, right: int) -> None:
        self.s.remove(left)
        del self.stoe[left]
        self.e.remove(right)
        del self.etos[right]

    def add(self, left: int, right: int) -> None:
        i = self.e.bisect_left(left)
        if 0 <= i < len(self.e):
            p = self.e[i]
            s = self.etos[p]
            self.remove(s, p)
            p += 1
        else:
            s = p = left
        for l in self.s.irange(left, right):
            self.c += l - p
            p = self.stoe[l]
            self.remove(s, p)
            p += 1
        self.c += right - p + 1

        self.s.add(left)
        self.stoe[left] = right
        self.e.add(right)
        self.etos[right] = left

    def count(self) -> int:
        return self.c


countIntervals = (
    CountIntervals()
)  # initialize the object with an empty set of intervals.
countIntervals.add(2, 3)  # add [2, 3] to the set of intervals.
countIntervals.add(7, 10)  # add [7, 10] to the set of intervals.
print(countIntervals.count())  # return 6
# the integers 2 and 3 are present in the interval [2, 3].
# the integers 7, 8, 9, and 10 are present in the interval [7, 10].
countIntervals.add(5, 8)  # add [5, 8] to the set of intervals.
print(countIntervals.count())  # return 8
# the integers 2 and 3 are present in the interval [2, 3].
# the integers 5 and 6 are present in the interval [5, 8].
# the integers 7 and 8 are present in the intervals [5, 8] and [7, 10].
# the integers 9 and 10 are present in the interval [7, 10].
