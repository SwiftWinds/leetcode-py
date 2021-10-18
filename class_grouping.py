def classGrouping(levels, maxSpread):
    # Write your code here
    # print(f"maxSpread: {maxSpread}; levels: {str(levels)[1:-1]}")
    levels.sort()
    groups = 0
    i = 0
    while i < len(levels):
        groups += 1
        j = i + 1
        while j < len(levels):
            if levels[j] - levels[i] > maxSpread:
                break
            j += 1
        i = j
    return groups


print(classGrouping([4, 8, 1, 7], 3))
print(classGrouping([1, 4, 7, 3, 4], 2))
print(classGrouping([4, 1, 2, 5, 3], 0))
