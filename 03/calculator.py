import math


def addition(x, y):
    try:
        x = float(x)
        y = float(y)
        result = x + y
        return result

    except Exception:
        raise ValueError('This operation is not supported for given input parameters')


def subtraction(x, y):
    try:
        x = float(x)
        y = float(y)
        return x - y

    except Exception:
        raise ValueError('This operation is not supported for given input parameters')


def multiplication(x, y):
    try:
        x = float(x)
        y = float(y)
        return x * y

    except Exception:
        raise ValueError('This operation is not supported for given input parameters')


def division(x, y):
    try:
        x = float(x)
        y = float(y)
        return x / y

    except Exception:
        raise ValueError('This operation is not supported for given input parameters')


def modulo(x, y):
    try:
        x = float(x)
        y = float(y)
        if y <= 0 or x < y:
            raise ValueError
        else:
            return x % y

    except Exception:
        raise ValueError('This operation is not supported for given input parameters')


def secondPower(x):
    try:
        x = float(x)
        return x * x

    except Exception:
        raise ValueError('This operation is not supported for given input parameters')


def power(x, y):
    try:
        x = float(x)
        y = float(y)
        if y < 0:
            raise ValueError
        else:
            return float(x ** y)

    except Exception:
        raise ValueError('This operation is not supported for given input parameters')


def secondRadix(x):
    try:
        x = float(x)
        if x <= 0:
            raise ValueError
        else:
            return math.sqrt(x)

    except Exception:
        raise ValueError('This operation is not supported for given input parameters')


def magic(x, y, z, k):
    try:
        l = addition(x, k)
        m = addition(y + z)
        return addition(division(l, m), 1)

    except Exception:
        raise ValueError('This operation is not supported for given input parameters')


def control(a, x, y, z, k):
    a = str(a)

    return {
        '1': addition(x, y),
        '2': subtraction(x, y),
        '3': multiplication(x, y),
        '4': division(x, y),
        '5': modulo(x, y),
        '6': power(x, y),
        '8': secondRadix(x),
        '9': magic(x, y, z, k),
    }[a]


def runTests():
    try:
        result = division(6, 2)
        expected = 3
        if result != expected:
            print('\n*/*/*/*/* UNEXPECTED RESULT */*/*/*/*')
            print('division(6, 2), expected: 3 actual: ' + str(result))
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
            print('division(\'3.5\', 2), expected: 1.75 actual: ' + str(result))
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
            print('power(5, 2), expected: 25 actual: ' + str(result))
            print('*/*/*/*/* UNEXPECTED RESULT */*/*/*/*\n')
    except ValueError:
        print('power(5, 2): ValueError')

    try:
        result = secondRadix(9)
        expected = 3
        if result != expected:
            print('\n*/*/*/*/* UNEXPECTED RESULT */*/*/*/*')
            print('secondRadix(9), expected: 3 actual: ' + str(result))
            print('*/*/*/*/* UNEXPECTED RESULT */*/*/*/*\n')
    except ValueError:
        print('secondRadix(9): ValueError')

    try:
        result = secondRadix(5.0625)
        expected = 2.25
        if result != expected:
            print('\n*/*/*/*/* UNEXPECTED RESULT */*/*/*/*')
            print('secondRadix(9), expected: 2.25 actual: ' + str(result))
            print('*/*/*/*/* UNEXPECTED RESULT */*/*/*/*\n')
    except ValueError:
        print('secondRadix(9): ValueError')

    try:
        control(9, 1, 2, 3, 4)
    except ValueError:
        print('control(9, 1, 2, 3, 4): ValueError')


runTests()
