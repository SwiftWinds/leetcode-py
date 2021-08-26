# zero = z: 1, e: 1, r: 1, o: 1 => z
# two = t: 1, w: 1, o: 1 => w
# four = f: 1, o: 1, u: 1, r: 1 => u
# six = s: 1, i: 1, x: 1 => x
# eight: e: 1, i: 1, g: 1, h: 1, t: 1 => g

# one = o: 1, n: 1, e: 1 => o
# three = t: 1, h: 1, r: 1, e: 2 => t, h, r
# five = f: 1, i: 1, v: 1, e: 1 => f
# seven: s: 1, e: 2, v: 1, n: 1 => s

# nine: n: 2, i: 1, e: 1 => n, i, e

num_specials = [(0, "z"), (2, "w"), (4, "u"), (6, "x"), (8, "g"), (1, "o"), (3, "t"), (5, "f"), (7, "s"), (9, "i")]

num_to_word = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

lines = ["reuonnoinfe", "fourtwozero", "onethreethreeseven"]
for line in lines:
    line = line.strip()
    letters = {}
    out = [0] * 10
    for letter in line:
        if letter not in letters:
            letters[letter] = 0
        letters[letter] += 1


    def count_num(num, letter):
        count = letters.get(letter, 0)
        out[num] = count
        num_word = num_to_word[num]
        if count > 0:
            for letter in num_word:
                letters[letter] -= count


    for num, special in num_specials:
        count_num(num, special)

    for i, num in enumerate(out):
        for _ in range(num):
            print(i, end="")

    print()
