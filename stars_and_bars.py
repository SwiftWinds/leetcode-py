import bisect


def starsAndBars(s, startIndex, endIndex):
    bars = []
    for i, ch in enumerate(s):
        if ch == "|":
            bars.append(i)

    res = []
    for s_idx, e_idx in zip(startIndex, endIndex):
        s_idx -= 1
        e_idx -= 1
        left = bisect.bisect_left(bars, s_idx)
        stars = 0
        i = left
        prev_idx = bars[left] - 1
        while i < len(bars) and bars[i] <= e_idx:
            cur_idx = bars[i]
            stars += cur_idx - prev_idx - 1
            prev_idx = cur_idx
            i += 1
        res.append(stars)
    return res


print(starsAndBars('*|*|', [1], [3]))
