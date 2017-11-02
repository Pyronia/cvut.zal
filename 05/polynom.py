def polyEval(poly, x):
    result = 0
    i = len(poly)

    while i > 0:
        result = result * x + poly[i]

    return result

def polySum(poly1, poly2):
    pass


def polyMultiply(poly1, poly2):
    pass


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