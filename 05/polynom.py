def polyEval(poly, x):
    result = 0
    i = len(poly)
    while i > 0:
        i -= 1
        result = result * x + poly[i]

    return result


def polySum(poly1, poly2):
    result = []
    isnotfirst = True

    if len(poly1) > len(poly2):
        i = len(poly1)
        while i > 0:
            i -= 1
            if i < len(poly2):
                coefficient = poly1[i] + poly2[i]
                if coefficient != 0 or isnotfirst:
                    result.append(coefficient)
                    isnotfirst = True

            else:
                result.append(poly1[i])

    else:
        i = len(poly2)
        while i > 0:
            i -= 1
            if i < len(poly1):
                coefficient = poly1[i] + poly2[i]
                if coefficient != 0 or isnotfirst:
                    result.append(coefficient)
                    isnotfirst = True

            else:
                result.append(poly2[i])

    result.reverse()
    return result


def polyMultiply(poly1, poly2):
    result = []

    for i in range(len(poly1) + len(poly2) - 1):
        result.append(0)

    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result[i + j] += poly1[i] * poly2[j]

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
