def polyEval(poly, x):
    result = 0
    i = len(poly) - 1
    while i > -1:
        result = result * x + poly[i]
        i -= 1

    return result


def polySum(poly1, poly2):
    if len(poly1) > len(poly2):
        for i in range(len(poly2)):
            poly1[i] += poly2[i]
        return poly1

    else:
        for i in range(len(poly1)):
            poly2[i] += poly1[i]
        return poly2


def polyMultiply(poly1, poly2):
    result = []
    for i in range(len(poly1) + len(poly2) - 1):
        result.append(0)

    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result[i + j] = poly1[i] * poly2[j]

    return result


def runTests():
    result = polyEval([1, 2.5, 3.5, 0, 5.4], 0)
    expected = 1
    if result != expected:
        print('\n*/*/*/*/* UNEXPECTED RESULT */*/*/*/*')
        print('polyEval([1, 2.5, 3.5, 0, 5.4], 0), expected: ' + str(expected) + ' actual: ' + str(result))
        print('*/*/*/*/* UNEXPECTED RESULT */*/*/*/*\n')

    result = polyEval([1, 2.5, 3.5, 0, 5.4], 2)
    expected = 106.4
    if result != expected:
        print('\n*/*/*/*/* UNEXPECTED RESULT */*/*/*/*')
        print('polyEval([1, 2.5, 3.5, 0, 5.4], 2), expected: ' + str(expected) + ' actual: ' + str(result))
        print('*/*/*/*/* UNEXPECTED RESULT */*/*/*/*\n')

    result = polySum([1, 2, 5], [2, 0, 1, -7])
    expected = [3, 2, 6, -7]
    if result != expected:
        print('\n*/*/*/*/* UNEXPECTED RESULT */*/*/*/*')
        print('polySum([1, 2, 5], [2, 0, 1, -7]), expected: ' + str(expected) + ' actual: ' + str(result))
        print('*/*/*/*/* UNEXPECTED RESULT */*/*/*/*\n')

    result = polyMultiply([1, 2, 5], [2, 0, 1, -7])
    expected = [2, 4, 11, -5, -9, -35]
    if result != expected:
        print('\n*/*/*/*/* UNEXPECTED RESULT */*/*/*/*')
        print('polyMultiply([1, 2, 5], [2, 0, 1, -7]), expected: ' + str(expected) + ' actual: ' + str(result))
        print('*/*/*/*/* UNEXPECTED RESULT */*/*/*/*\n')


runTests()
