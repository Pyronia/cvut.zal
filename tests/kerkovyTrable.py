def is_factor(f, n):
    return n % f == 0


def is_multiple(m, n):
    return is_factor(n, m)


print(is_multiple(12, 3))
