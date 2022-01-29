class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7
        mem = {}
        def sub(ch, left):
            if left == 1:
                return 1
            if (ch, left) in mem:
                return mem[(ch, left)]
            if ch == 'a':
                res = mem[(ch, left)] = sub('e', left - 1) % mod
                return res
            if ch == 'e':
                res = mem[(ch, left)] = (sub('a', left - 1) + sub('i', left - 1)) % mod
                return res
            if ch == 'i':
                res = mem[(ch, left)] = (sub('a', left - 1) + sub('e', left - 1) + sub('o', left - 1) + sub('u', left - 1)) % mod
                return res
            if ch == 'o':
                res = mem[(ch, left)] = (sub('i', left - 1) + sub('u', left - 1)) % mod
                return res
            if ch == 'u':
                res = mem[(ch, left)] = sub('a', left - 1) % mod
                return res
        return (sub('a', n) + sub('e', n) + sub('i', n) + sub('o', n) + sub('u', n)) % mod
