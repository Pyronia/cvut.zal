def runTests():
    try:
        result = division(6, 2)
        expected = 3
        if result != expected:
            print('\n*/*/*/*/* UNEXPECTED RESULT */*/*/*/*')
            print('division(6, 2), expected: ' + str(expected) + ' actual: ' + str(result))
            print('*/*/*/*/* UNEXPECTED RESULT */*/*/*/*\n')
    except ValueError:
        print('\n*/*/*/*/* UNEXPECTED ERROR */*/*/*/*')
        print('division(6, 2)')
        print('*/*/*/*/* UNEXPECTED ERROR */*/*/*/*\n')

    try:
        result = division('3.5', 2)
        expected = 1.75
        if result != expected:
            print('\n*/*/*/*/* UNEXPECTED RESULT */*/*/*/*')
            print('division(\'3.5\', 2), expected: ' + str(expected) + ' actual: ' + str(result))
            print('*/*/*/*/* UNEXPECTED RESULT */*/*/*/*\n')
    except ValueError:
        print('\n*/*/*/*/* UNEXPECTED ERROR */*/*/*/*')
        print('division(\'3.5\', 2)')
        print('*/*/*/*/* UNEXPECTED ERROR */*/*/*/*\n')

    try:
        result = division(1, 0)
        print('\n*/*/*/*/* UNEXPECTED RESULT */*/*/*/*')
        print('division(1, 0), result: ' + str(result))
        print('*/*/*/*/* UNEXPECTED RESULT */*/*/*/*\n')
    except ValueError:
        print('division(1, 0): ValueError')

    try:
        division('str', 0)
    except ValueError:
        print('division(\'str\', 0): ValueError')

    try:
        result = power(5, 2)
        expected = 25
        if result != expected:
            print('\n*/*/*/*/* UNEXPECTED RESULT */*/*/*/*')
            print('power(5, 2), expected: ' + str(expected) + ' actual: ' + str(result))
            print('*/*/*/*/* UNEXPECTED RESULT */*/*/*/*\n')
    except ValueError:
        print('power(5, 2): ValueError')

    try:
        result = secondRadix(9)
        expected = 3
        if result != expected:
            print('\n*/*/*/*/* UNEXPECTED RESULT */*/*/*/*')
            print('secondRadix(9), expected: ' + str(expected) + ' actual: ' + str(result))
            print('*/*/*/*/* UNEXPECTED RESULT */*/*/*/*\n')
    except ValueError:
        print('secondRadix(9): ValueError')

    try:
        result = secondRadix(5.0625)
        expected = 2.25
        if result != expected:
            print('\n*/*/*/*/* UNEXPECTED RESULT */*/*/*/*')
            print('secondRadix(9), expected: ' + str(expected) + ' actual: ' + str(result))
            print('*/*/*/*/* UNEXPECTED RESULT */*/*/*/*\n')
    except ValueError:
        print('secondRadix(9): ValueError')

    try:
        result = control('ADDITION', 2, 3, 4, 5)
        expected = 5
        if result != expected:
            print('\n*/*/*/*/* UNEXPECTED RESULT */*/*/*/*')
            print('control(\'ADDITION\', 2, 3, 4, 5), expected: ' + str(expected) + ' actual: ' + str(result))
            print('*/*/*/*/* UNEXPECTED RESULT */*/*/*/*\n')
    except ValueError:
        print('control(\'ADDITION\', 2, 3, 4, 5): ValueError')

    try:
        result = control('ADDITION', -1, 1, 1, -1)
        expected = 0
        if result != expected:
            print('\n*/*/*/*/* UNEXPECTED RESULT */*/*/*/*')
            print('control(\'ADDITION\', -1, 1, 1, -1), expected: ' + str(expected) + ' actual: ' + str(result))
            print('*/*/*/*/* UNEXPECTED RESULT */*/*/*/*\n')
    except ValueError:
        print('control(\'ADDITION\', -1, 1, 1, -1): ValueError')

    try:
        result = control('SUBTRACTION', 2, 3, 4, 5)
        expected = -1
        if result != expected:
            print('\n*/*/*/*/* UNEXPECTED RESULT */*/*/*/*')
            print('control(\'SUBTRACTION\', 2, 3, 4, 5), expected: ' + str(expected) + ' actual: ' + str(result))
            print('*/*/*/*/* UNEXPECTED RESULT */*/*/*/*\n')
    except ValueError:
        print('control(\'SUBTRACTION\', 2, 3, 4, 5): ValueError')


runTests()
