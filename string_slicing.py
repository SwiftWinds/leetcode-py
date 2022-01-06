from collections import Counter
from enum import Enum


class State(Enum):
    FIRST_PARTITION = 1
    FIRST_B_COUNTER = 2
    SECOND_PARTITION = 3
    SECOND_B_COUNTER = 4


def solution(S):
    S_counter = Counter(S)
    if S_counter['a'] % 3 != 0:
        return 0
    if S_counter['a'] == 0:
        n = len(S) - 2
        return 0 if n <= 0 else n * (n + 1) // 2
    as_per_partition = S_counter['a'] / 3
    num_as = 0
    slices = [1] * 2
    state = State.FIRST_PARTITION

    def found_a(next_state):
        nonlocal num_as, state
        num_as += 1
        if as_per_partition == num_as:
            num_as = 0
            state = next_state

    for i, ch in enumerate(S):
        if state == State.FIRST_PARTITION:
            if ch == "a":
                found_a(State.FIRST_B_COUNTER)
        elif state == State.FIRST_B_COUNTER:
            if ch == "b":
                slices[0] += 1
            else:
                state = State.SECOND_PARTITION
                found_a(State.SECOND_B_COUNTER)
        elif state == State.SECOND_PARTITION:
            if ch == "a":
                found_a(State.SECOND_B_COUNTER)
        elif state == State.SECOND_B_COUNTER:
            if ch == "b":
                slices[1] += 1
            else:
                break
    return slices[0] * slices[1]
