from collections import deque


def findRemainingPolicies(direction, length):
    q = deque()
    for i, el in enumerate(zip(direction, length)):
        d, l = el
        to_insert = True
        while q:
            prev_d, prev_l = q[-1][:2]
            if not (prev_d == 1 and d == -1):
                break
            if prev_l > l:
                to_insert = False
                break
            elif prev_l == l:
                to_insert = False
                q.pop()
                break
            else:
                q.pop()
        if to_insert:
            q.append((d, l, i))

    res = []
    for d, l, i in q:
        res.append(i)

    return res


findRemainingPolicies(direction=[-1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1],
                      length=[503879204, 170167325, 336244598, 340588577, 574069670, 867487718, 960463404, 503879204,
                              783394187, 986771195, 971971259, 502605091, 574069670, 589992928, 352607458, 772764137])
