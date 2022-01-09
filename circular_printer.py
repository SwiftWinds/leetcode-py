def time_betw_chars(a, b):
    if a < b:
        left_char = a
        right_char = b
    else:
        left_char = b
        right_char = a
    right_length = ord(right_char) - ord(left_char)
    left_length = ord(left_char) + (26 - ord(right_char))
    return min(left_length, right_length)


def getTime(s):
    s = 'A' + s
    tot = 0
    for a, b in zip(s, s[1:]):
        tot += time_betw_chars(a, b)
    return tot


assert getTime('AZGB') == 13
