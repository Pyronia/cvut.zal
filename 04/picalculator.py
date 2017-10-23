def newtonPi(init):
    pass


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
        iteration =+ 1
        odd = not odd

    print('Iterations = ' + str(iterations))
    return pi


def nilakanthaPi(iterations):
    dividend = 4
    divisor = 2
    iteration = 0
    pi = 3
    odd = True

    while iteration < iterations:
        if odd:
            pi += dividend / divisor * (divisor + 1) * (divisor + 2)
        else:
            pi -= dividend / divisor * (divisor + 1) * (divisor + 2)

        divisor += 2
        iteration += 1
        odd = not odd

    print('Iterations = ' + str(iterations))
    return pi

def testNewtonPi(init):
    pass


def testLeibnizPi(iterations):
    print("Expected iterations = " + str(iterations) +
          "\nPi = " + str(leibnizPi(iterations)))


def testNilakanthaPi(iterations):
    print("Expected iterations = " + str(iterations) +
          "\nPi = " + str(testNilakanthaPi(iterations)))


testLeibnizPi(5000000)
testNilakanthaPi(5000000)
