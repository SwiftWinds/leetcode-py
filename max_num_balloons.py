from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """
        Count the max number of times the word 'balloon' can be constructed from the text.
        """
        text_counter = Counter(text)
        balloon_counter = Counter('balloon')
        return min(text_counter[char] // balloon_counter[char] for char in balloon_counter)
