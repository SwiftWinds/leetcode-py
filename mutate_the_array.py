def mutateTheArray(n, a):
    b = []
    for i, el in enumerate(a):
        tot = el
        if i - 1 >= 0:
            tot += a[i - 1]
        if i + 1 <= n - 1:
            tot += a[i + 1]
        b.append(tot)
    return b
