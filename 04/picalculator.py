from math import sin
from math import cos


def newtonPi(k):
    kPlusOne = k - sin(k) / cos(k)

    while kPlusOne != k:
        k = kPlusOne
        kPlusOne = kPlusOne - sin(kPlusOne) / cos(kPlusOne)

    return kPlusOne


def leibnizPi(iterations):
    dividend = 4
    divisor = 1
    iteration = 0
    pi = 0
    odd = True

    while iteration < iterations:
        if odd:
            pi += dividend / divisor
        else:
            pi -= dividend / divisor

        divisor += 2
        iteration += 1
        odd = not odd

    print('Iterations = ' + str(iterations))
    return pi


def nilakanthaPi(iterations):
    dividend = 4
    divisor = 2
    iteration = 1
    pi = 3
    odd = True

    while iteration < iterations:
        if odd:
            pi += dividend / (divisor * (divisor + 1) * (divisor + 2))
        else:
            pi -= dividend / (divisor * (divisor + 1) * (divisor + 2))

        divisor += 2
        iteration += 1
        odd = not odd

    print('Iterations = ' + str(iterations))
    return pi


def testNewtonPi(init):
    print("\nTest Newton Pi:")
    print("\nPi = " + str(newtonPi(init)))


def testLeibnizPi(iterations):
    print("\nTest Leibniz Pi:")
    print("Expected iterations = " + str(iterations) +
          "\nPi = " + str(leibnizPi(iterations)))


def testNilakanthaPi(iterations):
    print("\nTest Nilakantha Pi:")
    print("Expected iterations = " + str(iterations) +
          "\nPi = " + str(nilakanthaPi(iterations)))


testLeibnizPi(5000000)
testNilakanthaPi(1)
testNewtonPi(-3.0)
