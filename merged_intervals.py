def getMergedIntervals(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    i = 0
    merged = []
    while i < len(intervals):
        interval = [*intervals[i]]
        j = i + 1
        while j < len(intervals):
            if intervals[j][0] > interval[1]:
                i = j
                merged.append(interval)
                break
            interval[1] = max(interval[1], intervals[j][1])
        else:
            break
    return merged
