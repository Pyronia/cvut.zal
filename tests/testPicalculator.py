def testNewtonPi(init):
    print("\nTest Newton Pi:")
    result = newtonPi(init)
    expected = -3.141592653589793
    if result != expected:
        print('\n*/*/*/*/* UNEXPECTED RESULT */*/*/*/*')
        print('testNewtonPi(-3.0), expected: ' + str(expected) + ' actual: ' + str(result))
        print('*/*/*/*/* UNEXPECTED RESULT */*/*/*/*\n')


def testLeibnizPi(iterations):
    print("\nTest Leibniz Pi:")
    result = leibnizPi(iterations)
    expected = 3.1415924535897797
    if result != expected:
        print('\n*/*/*/*/* UNEXPECTED RESULT */*/*/*/*')
        print('testLeibnizPi(5000000), expected: ' + str(expected) + ' actual: ' + str(result))
        print('*/*/*/*/* UNEXPECTED RESULT */*/*/*/*\n')


def testNilakanthaPi(iterations):
    print("\nTest Nilakantha Pi:")
    result = nilakanthaPi(1)
    expected = 3
    if result != expected:
        print('\n*/*/*/*/* UNEXPECTED RESULT */*/*/*/*')
        print('testNilakanthaPi(1), expected: ' + str(expected) + ' actual: ' + str(result))
        print('*/*/*/*/* UNEXPECTED RESULT */*/*/*/*\n')


testLeibnizPi(5000000)
testNilakanthaPi(1)
testNewtonPi(-3.0)